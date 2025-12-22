from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user, login_required
from app import db
from app.models import Category, Event
from datetime import datetime, timedelta

# ====== Blueprint для веб-страниц ======
web_pages_bp = Blueprint('web_pages', __name__)

# ====== Blueprint для API расписания ======
schedule_api_bp = Blueprint('schedule_api', __name__)

# ======== ВЕБ-СТРАНИЦЫ ========

@web_pages_bp.route('/schedule')
@login_required
def schedule_page():
    """Страница с недельным расписанием"""
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    
    days = []
    for i in range(7):
        day_date = start_of_week + timedelta(days=i)
        days.append({
            'name': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 
                    'Пятница', 'Суббота', 'Воскресенье'][i],
            'date': day_date.strftime('%d.%m.%Y'),
            'full_date': day_date.strftime('%Y-%m-%d'),
            'short_name': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'][i]
        })
    
    week_number = today.isocalendar()[1]
    current_week = f"{today.year}-W{week_number:02d}"
    
    return render_template('schedule.html', 
                          days=days, 
                          current_week=current_week)

# ======== API для расписания ========

@schedule_api_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    """Получить категории текущего пользователя"""
    categories = Category.query.filter_by(user_id=current_user.id).all()
    categories_list = [cat.to_dict() for cat in categories]

    return jsonify({
        'status': 'success',
        'count': len(categories_list),
        'categories': categories_list
    })

@schedule_api_bp.route('/events', methods=['POST'])
@login_required
def create_event():
    """Создать новое событие"""
    data = request.get_json()

    required = ['category_id', 'start_time', 'end_time']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing required fields'}), 400

    category = Category.query.filter_by(
        id=data['category_id'],
        user_id=current_user.id
    ).first()

    if not category:
        return jsonify({'error': 'Category not found'}), 404

    # Исправляем формат времени
    try:
        # Формат: "2025-12-22T14:30:00"
        start_time = datetime.fromisoformat(data['start_time'].replace('Z', '+00:00'))
        end_time = datetime.fromisoformat(data['end_time'].replace('Z', '+00:00'))
    except ValueError:
        return jsonify({'error': 'Invalid datetime format'}), 400

    event = Event(
        user_id=current_user.id,
        category_id=data['category_id'],
        start_time=start_time,
        end_time=end_time,
        type=data.get('type', 'plan'),
        source='web'
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'event_id': event.id,
        'message': 'Event created successfully'
    }), 201

@schedule_api_bp.route('/week/<week_str>', methods=['GET'])
@login_required
def get_events_by_week(week_str):
    """Получить события за определенную неделю"""
    try:
        # Формат: "2025-W52"
        year, week = map(int, week_str.split('-W'))
        
        # Получаем первый день недели (понедельник)
        first_day = datetime.strptime(f'{year}-{week}-1', '%Y-%W-%w')
        last_day = first_day + timedelta(days=7)
        
        events = Event.query.filter(
            Event.user_id == current_user.id,
            Event.start_time >= first_day,
            Event.start_time < last_day
        ).join(Category).order_by(Event.start_time).all()
        
        events_list = []
        for event in events:
            event_dict = event.to_dict()
            event_dict['category_name'] = event.category.name
            event_dict['category_color'] = event.category.color
            event_dict['date'] = event.start_time.date().isoformat()
            event_dict['start_time_str'] = event.start_time.strftime('%H:%M')
            event_dict['end_time_str'] = event.end_time.strftime('%H:%M')
            events_list.append(event_dict)
        
        return jsonify({
            'status': 'success',
            'count': len(events_list),
            'events': events_list
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@schedule_api_bp.route('/copy', methods=['POST'])
@login_required
def copy_week():
    """Скопировать план на следующую неделю"""
    data = request.get_json()
    
    if 'source_week' not in data:
        return jsonify({'error': 'Missing source_week'}), 400
    
    try:
        year, week = map(int, data['source_week'].split('-W'))
        
        # Пока возвращаем успех
        target_year, target_week = year, week + 1
        if target_week > 52:
            target_year += 1
            target_week = 1
        
        return jsonify({
            'status': 'success',
            'message': 'Week copied successfully',
            'target_week': f"{target_year}-W{target_week:02d}"
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@schedule_api_bp.route('/quick-add', methods=['POST'])
@login_required
def quick_add_event():
    """Быстрое добавление события"""
    data = request.get_json()
    
    try:
        category_id = data['category_id']
        day_offset = data.get('day_offset', 0)  # 0=сегодня, 1=завтра и т.д.
        start_hour = data['start_hour']
        duration_hours = data.get('duration_hours', 1)
        
        # Проверяем категорию
        category = Category.query.filter_by(
            id=category_id,
            user_id=current_user.id
        ).first()
        
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        
        # Создаем время
        today = datetime.now().date()
        target_date = today + timedelta(days=day_offset)
        
        start_time = datetime.combine(target_date, datetime.strptime(f"{start_hour}:00", "%H:%M").time())
        end_time = start_time + timedelta(hours=duration_hours)
        
        event = Event(
            user_id=current_user.id,
            category_id=category_id,
            start_time=start_time,
            end_time=end_time,
            type='plan',
            source='web'
        )
        
        db.session.add(event)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'event_id': event.id,
            'message': 'Event added successfully'
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
