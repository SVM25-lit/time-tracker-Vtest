# app/routes/web_routes.py
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app import db
from app.models import Category, Event
from datetime import datetime

web_bp = Blueprint('web', __name__, url_prefix='/api/v1')


@web_bp.route('/categories', methods=['GET'])
@login_required  # Только для авторизованных
def get_categories():
    """Получить ВСЕ категории текущего пользователя"""

    # current_user доступен благодаря flask_login
    categories = Category.query.filter_by(user_id=current_user.id).all()

    # Используем метод to_dict() из модели
    categories_list = [cat.to_dict() for cat in categories]

    return jsonify({
        'status': 'success',
        'count': len(categories_list),
        'categories': categories_list
    })

#тут я покопалась
@web_bp.route('/events', methods=['POST'])
@login_required
def create_event():
    """Создать новое событие (план) из веб-интерфейса"""
    data = request.get_json()

    # Проверяем обязательные поля
    required = ['category_id', 'start_time', 'end_time']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing required fields'}), 400

    # Проверяем, что категория принадлежит пользователю
    category = Category.query.filter_by(
        id=data['category_id'],
        user_id=current_user.id
    ).first()

    if not category:
        return jsonify({'error': 'Category not found'}), 404

    # Создаём событие (по умолчанию type='plan', source='web')
    event = Event(
        user_id=current_user.id,
        category_id=data['category_id'],
        start_time=datetime.fromisoformat(data['start_time']),
        end_time=datetime.fromisoformat(data['end_time']),
        type=data.get('type', 'plan'),  # По умолчанию 'plan'
        source='web'  # Событие из веб-интерфейса
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'event_id': event.id,
        'message': 'Event created successfully'
    }), 201

#Это моё

@web_bp.route('/schedule')
@login_required
def schedule():
    """Страница с недельным расписанием"""
    import datetime
    
    # Получаем текущую неделю
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    
    # Создаем список дней недели
    days = []
    for i in range(7):
        day_date = start_of_week + datetime.timedelta(days=i)
        days.append({
            'name': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'][i],
            'date': day_date.strftime('%d.%m'),
            'full_date': day_date.strftime('%Y-%m-%d')
        })
    
    # Формат для input type="week"
    week_number = today.isocalendar()[1]
    current_week = f"{today.year}-W{week_number:02d}"
    
    return render_template('schedule.html', 
                          days=days, 
                          current_week=current_week)

#Это тоже
@web_bp.route('/api/v1/events/week/<week_str>', methods=['GET'])
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
        
        events_list = [event.to_dict() for event in events]
        
        return jsonify({
            'status': 'success',
            'count': len(events_list),
            'events': events_list  # ← Добавить ключ и значение
        })
    except Exception as e:  # ← ДОБАВИТЬ ЭТО
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
