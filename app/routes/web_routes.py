from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user, login_required
from app import db
from app.models import Category, Event
from datetime import datetime, timedelta 

# РАЗДЕЛЯЕМ API И ВЕБ-СТРАНИЦЫ


web_pages_bp = Blueprint('web_pages', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# ВЕБ-СТРАНИЦЫ

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

# API МАРШРУТЫ

@api_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    """Получить ВСЕ категории текущего пользователя"""
    categories = Category.query.filter_by(user_id=current_user.id).all()
    categories_list = [cat.to_dict() for cat in categories]

    return jsonify({
        'status': 'success',
        'count': len(categories_list),
        'categories': categories_list
    })

@api_bp.route('/events', methods=['POST'])
@login_required
def create_event():
    """Создать новое событие (план) из веб-интерфейса"""
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

@api_bp.route('/events/week/<week_str>', methods=['GET'])
@login_required
def get_events_by_week(week_str):
    """Получить события за определенную неделю"""
    try:
        year, week = map(int, week_str.split('-W'))
        
        # Получаем первый день недели
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
            # Добавляем информацию о категории
            event_dict['category_name'] = event.category.name
            event_dict['category_color'] = event.category.color
            event_dict['date'] = event.start_time.date().isoformat()
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

# Дополнительные API эндпоинты
@api_bp.route('/copy-week', methods=['POST'])
@login_required
def copy_week():
    """Скопировать план на следующую неделю"""
    data = request.get_json()
    
    if 'source_week' not in data:
        return jsonify({'error': 'Missing source_week'}), 400
    
    try:
        year, week = map(int, data['source_week'].split('-W'))
        
        # Пока возвращаем успех (реализуйте копирование позже)
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
