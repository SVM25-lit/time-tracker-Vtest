{% extends "base.html" %}

{% block title %}Расписание - Time Tracker{% endblock %}

{% block extra_css %}
<style>
    .schedule-container {
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        overflow: hidden;
        margin-bottom: 2rem;
        overflow-x: auto;
    }
    
    .schedule-header {
        background-color: var(--primary-color);
        color: white;
        padding: 1rem;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .schedule-table {
        min-width: 1400px;
        border-collapse: separate;
        border-spacing: 0;
    }
    
    .time-column {
        width: 80px;
        background-color: #f8f9fa;
        font-size: 0.85rem;
        color: #666;
        text-align: center;
        vertical-align: top;
        padding: 0.5rem;
        border-right: 1px solid #dee2e6;
        position: sticky;
        left: 0;
        z-index: 50;
    }
    
    .day-column {
        width: 200px;
        vertical-align: top;
        border-right: 1px solid #dee2e6;
    }
    
    .day-header {
        background-color: #e9ecef;
        padding: 0.75rem;
        font-weight: 600;
        text-align: center;
        border-bottom: 2px solid #dee2e6;
        position: sticky;
        top: 60px;
        z-index: 80;
    }
    
    .plan-header {
        background-color: #d1e7dd;
        color: #0f5132;
        padding: 0.5rem;
        text-align: center;
        font-size: 0.9rem;
        border-bottom: 1px solid #badbcc;
    }
    
    .fact-header {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 0.5rem;
        text-align: center;
        font-size: 0.9rem;
        border-bottom: 1px solid #bee5eb;
    }
    
    .time-slot {
        height: 40px;
        border-bottom: 1px solid #f0f0f0;
        position: relative;
    }
    
    .plan-cell, .fact-cell {
        height: 100%;
        padding: 2px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .plan-cell:hover {
        background-color: #e8f5e8;
    }
    
    .fact-cell:hover {
        background-color: #e8f5f5;
    }
    
    .plan-event, .fact-event {
        border-radius: 4px;
        padding: 3px 6px;
        margin: 1px;
        font-size: 0.8rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: pointer;
        border-left: 3px solid;
    }
    
    .plan-event {
        background-color: rgba(25, 135, 84, 0.1);
        border-color: #198754;
    }
    
    .fact-event {
        background-color: rgba(13, 110, 253, 0.1);
        border-color: #0d6efd;
    }
    
    .current-time {
        background-color: rgba(255, 193, 7, 0.1);
        position: relative;
    }
    
    .current-time::after {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 2px;
        background-color: #ffc107;
        z-index: 10;
    }
    
    .hour-marker {
        background-color: #f8f9fa;
        font-weight: 600;
    }
    
    .schedule-controls {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    
    .legend-item {
        display: inline-flex;
        align-items: center;
        margin-right: 1rem;
    }
    
    .legend-color {
        width: 16px;
        height: 16px;
        border-radius: 3px;
        margin-right: 0.5rem;
    }
    
    .category-color {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 5px;
        vertical-align: middle;
    }
    
    .modal-time-input {
        max-width: 150px;
    }
    
    /* Графики и статистика */
    .charts-container {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-top: 2rem;
    }
    
    .chart-card {
        height: 100%;
        padding: 1rem;
        border-radius: 10px;
        background: #f8f9fa;
        border: 1px solid #e9ecef;
    }
    
    .chart-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: var(--primary-color);
    }
    
    .chart-placeholder {
        height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
        border-radius: 8px;
        border: 2px dashed #dee2e6;
        color: #6c757d;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .stat-item {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid var(--primary-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #6c757d;
        margin-bottom: 0.5rem;
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-color);
    }
    
    .category-distribution {
        margin-top: 1.5rem;
    }
    
    .category-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0;
        border-bottom: 1px solid #f0f0f0;
    }
    
    .category-bar {
        height: 8px;
        background: var(--primary-color);
        border-radius: 4px;
        margin: 0.5rem 0;
    }
    
    @media (max-width: 768px) {
        .schedule-container {
            border-radius: 10px;
        }
        
        .schedule-controls {
            padding: 0.75rem;
        }
        
        .charts-container {
            padding: 1rem;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
{% endblock %}

{% block content %}
<div class="fade-in">
    <!-- Панель управления -->
    <div class="schedule-controls">
        <div class="d-flex justify-content-between align-items-center flex-wrap">
            <div>
                <h6 class="mb-2">Легенда:</h6>
                <div class="legend-item">
                    <span class="legend-color" style="background-color: #d1e7dd;"></span>
                    <span>План</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color" style="background-color: #d1ecf1;"></span>
                    <span>Факт</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color" style="background-color: #fff3cd;"></span>
                    <span>Текущее время</span>
                </div>
            </div>
            <div>
                <div class="input-group" style="max-width: 300px;">
                    <span class="input-group-text"><i class="bi bi-calendar-week"></i></span>
                    <input type="week" class="form-control" id="weekPicker" value="{{ current_week }}">
                    <button class="btn btn-outline-secondary" type="button" id="prevWeekBtn">
                        <i class="bi bi-chevron-left"></i>
                    </button>
                    <button class="btn btn-outline-secondary" type="button" id="nextWeekBtn">
                        <i class="bi bi-chevron-right"></i>
                    </button>
                    <button class="btn btn-outline-primary" type="button" id="currentWeekBtn">
                        Сегодня
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Основная таблица расписания -->
    <div class="schedule-container">
        <div class="schedule-header">
            <h5 class="mb-0">Недельное расписание (шаг 15 минут)</h5>
            <small class="opacity-75">4:00 - 22:30</small>
        </div>
        
        <div class="table-responsive">
            <table class="schedule-table">
                <thead>
                    <tr>
                        <th class="time-column">Время</th>
                        {% for day in days %}
                        <th class="day-column">
                            <div class="day-header">
                                {{ day.name }}<br>
                                <small>{{ day.date }}</small>
                            </div>
                            <div class="plan-header">План</div>
                            <div class="fact-header">Факт</div>
                        </th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody id="scheduleBody">
                    <!-- Время будет заполнено JavaScript -->
                </tbody>
            </table>
        </div>
    </div>
    
    <!-- Графики и статистика -->
    <div class="charts-container">
        <h4 class="mb-4">Статистика и аналитика</h4>
        
        <div class="row mb-4">
            <div class="col-md-8">
                <div class="chart-card">
                    <div class="chart-title">Выполнение плана по дням недели</div>
                    <div class="chart-placeholder" id="weeklyChart">
                        <div class="text-center">
                            <i class="bi bi-bar-chart" style="font-size: 3rem; opacity: 0.3;"></i>
                            <p class="mt-2">График загрузки данных...</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="chart-card">
                    <div class="chart-title">Общая статистика</div>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <div class="stat-label">Выполнено сегодня</div>
                            <div class="stat-value" id="todayPercentage">0%</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Выполнено за неделю</div>
                            <div class="stat-value" id="weekPercentage">0%</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Всего часов</div>
                            <div class="stat-value" id="totalHours">0ч</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Событий</div>
                            <div class="stat-value" id="totalEvents">0</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-6">
                <div class="chart-card">
                    <div class="chart-title">Распределение по категориям</div>
                    <div class="category-distribution" id="categoryDistribution">
                        <div class="text-center py-4 text-muted">
                            <i class="bi bi-pie-chart" style="font-size: 2rem; opacity: 0.3;"></i>
                            <p class="mt-2">Нет данных для отображения</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="chart-card">
                    <div class="chart-title">Быстрые действия</div>
                    <div class="d-grid gap-2 mt-3">
                        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addEventModal">
                            <i class="bi bi-plus-circle me-2"></i>Добавить событие
                        </button>
                        <button class="btn btn-outline-primary" id="copyWeekBtn">
                            <i class="bi bi-copy me-2"></i>Скопировать неделю
                        </button>
                        <button class="btn btn-outline-success" id="addCategoryBtn">
                            <i class="bi bi-tag me-2"></i>Новая категория
                        </button>
                        <button class="btn btn-outline-info" id="exportDataBtn">
                            <i class="bi bi-download me-2"></i>Экспорт данных
                        </button>
                    </div>
                    <div class="mt-4">
                        <h6 class="mb-2">Последние события</h6>
                        <div id="recentEvents">
                            <div class="text-muted text-center py-2">
                                <small>Нет последних событий</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Модальные окна (оставить как есть) -->
<div class="modal fade" id="addEventModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Добавить событие</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form id="addEventForm">
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Тип события</label>
                            <div class="btn-group w-100" role="group">
                                <input type="radio" class="btn-check" name="eventType" id="typePlan" value="plan" checked>
                                <label class="btn btn-outline-success" for="typePlan">План</label>
                                
                                <input type="radio" class="btn-check" name="eventType" id="typeFact" value="fact">
                                <label class="btn btn-outline-primary" for="typeFact">Факт</label>
                            </div>
                        </div>
                        
                        <div class="col-md-6 mb-3">
                            <label for="categorySelect" class="form-label">Категория</label>
                            <select class="form-select" id="categorySelect" required>
                                <option value="">Выберите категорию</option>
                                <!-- Категории будут заполнены через JavaScript -->
                            </select>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="startDate" class="form-label">Дата начала</label>
                            <input type="date" class="form-control" id="startDate" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="startTime" class="form-label">Время начала</label>
                            <select class="form-select" id="startTime" required>
                                <!-- Время будет заполнено JavaScript -->
                            </select>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="endDate" class="form-label">Дата окончания</label>
                            <input type="date" class="form-control" id="endDate" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="endTime" class="form-label">Время окончания</label>
                            <select class="form-select" id="endTime" required>
                                <!-- Время будет заполнено JavaScript -->
                            </select>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label for="eventDescription" class="form-label">Описание (необязательно)</label>
                        <textarea class="form-control" id="eventDescription" rows="2" placeholder="Дополнительные детали..."></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отмена</button>
                    <button type="submit" class="btn btn-primary">Добавить событие</button>
                </div>
            </form>
        </div>
    </div>
</div>

<div class="modal fade" id="categoryModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Новая категория</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form id="categoryForm">
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="categoryName" class="form-label">Название категории</label>
                        <input type="text" class="form-control" id="categoryName" required placeholder="Например: Работа, Учёба, Спорт...">
                    </div>
                    
                    <div class="mb-3">
                        <label for="categoryColor" class="form-label">Цвет категории</label>
                        <div class="d-flex flex-wrap gap-2" id="colorPicker">
                            <!-- Цвета будут добавлены JavaScript -->
                        </div>
                        <input type="hidden" id="selectedColor" value="#4361ee" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="categoryDescription" class="form-label">Описание (необязательно)</label>
                        <textarea class="form-control" id="categoryDescription" rows="2" placeholder="Описание категории..."></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отмена</button>
                    <button type="submit" class="btn btn-primary">Создать категорию</button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
document.addEventListener('DOMContentLoaded', function() {
    const scheduleBody = document.getElementById('scheduleBody');
    const weekPicker = document.getElementById('weekPicker');
    const currentWeekBtn = document.getElementById('currentWeekBtn');
    const prevWeekBtn = document.getElementById('prevWeekBtn');
    const nextWeekBtn = document.getElementById('nextWeekBtn');
    const copyWeekBtn = document.getElementById('copyWeekBtn');
    const addCategoryBtn = document.getElementById('addCategoryBtn');
    const exportDataBtn = document.getElementById('exportDataBtn');
    const colorPicker = document.getElementById('colorPicker');
    const categorySelect = document.getElementById('categorySelect');
    const categoryDistribution = document.getElementById('categoryDistribution');
    const recentEvents = document.getElementById('recentEvents');
    const weeklyChart = document.getElementById('weeklyChart');
    
    // Конфигурация времени
    const START_HOUR = 4;
    const END_HOUR = 22.5; // 22:30
    const TIME_SLOT_MINUTES = 15;
    
    let categories = [];
    let events = [];
    
    // Инициализация
    initSchedule();
    loadCategories();
    loadEvents();
    initColorPicker();
    initTimeSelects();
    initModalDates();
    
    // Основные функции (оставляем без изменений)
    function initSchedule() {
        scheduleBody.innerHTML = '';
        
        for (let hour = START_HOUR; hour < END_HOUR; hour += 0.25) {
            const hourInt = Math.floor(hour);
            const minute = (hour - hourInt) * 60;
            
            const timeString = `${hourInt.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
            const isHourMark = minute === 0;
            
            const row = document.createElement('tr');
            
            if (isHourMark) {
                row.classList.add('hour-marker');
            }
            
            // Проверка текущего времени
            const now = new Date();
            const currentHour = now.getHours() + now.getMinutes() / 60;
            if (Math.abs(currentHour - hour) < 0.125) {
                row.classList.add('current-time');
            }
            
            // Колонка времени
            const timeCell = document.createElement('td');
            timeCell.className = 'time-column';
            timeCell.textContent = timeString;
            row.appendChild(timeCell);
            
            // Колонки для каждого дня
            for (let i = 0; i < 7; i++) {
                const planCell = document.createElement('td');
                planCell.className = 'plan-cell';
                planCell.dataset.time = timeString;
                planCell.dataset.day = i;
                planCell.dataset.type = 'plan';
                planCell.addEventListener('click', handleCellClick);
                
                const factCell = document.createElement('td');
                factCell.className = 'fact-cell';
                factCell.dataset.time = timeString;
                factCell.dataset.day = i;
                factCell.dataset.type = 'fact';
                factCell.addEventListener('click', handleCellClick);
                
                const dayCell = document.createElement('td');
                dayCell.className = 'day-column';
                dayCell.appendChild(planCell);
                dayCell.appendChild(factCell);
                
                row.appendChild(dayCell);
            }
            
            scheduleBody.appendChild(row);
        }
    }
    
    function handleCellClick(event) {
        const cell = event.currentTarget;
        const time = cell.dataset.time;
        const day = parseInt(cell.dataset.day);
        const type = cell.dataset.type;
        
        // Получаем дату из выбранной недели
        const [year, week] = weekPicker.value.split('-W');
        const date = getDateFromWeek(year, week, day);
        
        // Показываем модальное окно с предзаполненными данными
        const modal = new bootstrap.Modal(document.getElementById('addEventModal'));
        
        // Устанавливаем тип события
        if (type === 'plan') {
            document.getElementById('typePlan').checked = true;
        } else {
            document.getElementById('typeFact').checked = true;
        }
        
        // Устанавливаем даты
        document.getElementById('startDate').value = date;
        document.getElementById('endDate').value = date;
        
        // Устанавливаем время
        document.getElementById('startTime').value = time;
        
        // Рассчитываем время окончания (+1 час по умолчанию)
        const [hours, minutes] = time.split(':').map(Number);
        let endHour = hours + 1;
        if (endHour >= END_HOUR) endHour = END_HOUR - 0.25;
        const endTime = `${endHour.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
        document.getElementById('endTime').value = endTime;
        
        modal.show();
    }
    
    function getDateFromWeek(year, week, day) {
        const simple = new Date(year, 0, 1 + (week - 1) * 7 + day);
        const dow = simple.getDay();
        const ISOweekStart = simple;
        
        if (dow <= 4) {
            ISOweekStart.setDate(simple.getDate() - simple.getDay() + 1 + day);
        } else {
            ISOweekStart.setDate(simple.getDate() + 8 - simple.getDay() + day);
        }
        
        return ISOweekStart.toISOString().split('T')[0];
    }
    
    function loadCategories() {
        console.log('Загрузка категорий...');
        
        // Пробуем разные пути API
        const apiPaths = [
            '/api/v1/schedule/categories',
            '/api/v1/categories',
            '/api/my/stats'
        ];
        
        let requestIndex = 0;
        
        function tryNextPath() {
            if (requestIndex >= apiPaths.length) {
                console.log('Все пути API недоступны, используем тестовые данные');
                loadTestCategories();
                return;
            }
            
            const path = apiPaths[requestIndex];
            console.log(`Пробуем путь: ${path}`);
            
            fetch(path)
                .then(response => {
                    console.log(`Ответ от ${path}: ${response.status}`);
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Данные категорий:', data);
                    
                    if (data.status === 'success' && data.categories) {
                        categories = data.categories;
                        updateCategorySelect();
                        updateCategoryDistribution();
                    } else if (data.categories) {
                        categories = data.categories;
                        updateCategorySelect();
                        updateCategoryDistribution();
                    } else {
                        console.warn('Неожиданный формат данных:', data);
                        loadTestCategories();
                    }
                })
                .catch(error => {
                    console.error(`Ошибка при запросе ${path}:`, error);
                    requestIndex++;
                    tryNextPath();
                });
        }
        
        tryNextPath();
    }
    
    function updateCategorySelect() {
        categorySelect.innerHTML = '<option value="">Выберите категорию</option>';
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.id;
            option.textContent = category.name;
            if (category.color) {
                option.dataset.color = category.color;
            }
            categorySelect.appendChild(option);
        });
        
        console.log('Обновлен список категорий, количество:', categories.length);
    }
    
    function loadEvents() {
        console.log('Загрузка событий...');
        
        const [year, week] = weekPicker.value.split('-W');
        const apiPaths = [
            `/api/v1/schedule/week/${year}-W${week}`,
            `/api/v1/events/week/${year}-W${week}`,
            '/api/my/events'
        ];
        
        let requestIndex = 0;
        
        function tryNextPath() {
            if (requestIndex >= apiPaths.length) {
                console.log('Все пути API недоступны, используем тестовые события');
                loadTestEvents();
                return;
            }
            
            const path = apiPaths[requestIndex];
            console.log(`Загрузка событий по пути: ${path}`);
            
            fetch(path)
                .then(response => {
                    console.log(`Ответ событий от ${path}: ${response.status}`);
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Данные событий:', data);
                    
                    if (data.status === 'success' && data.events) {
                        events = data.events;
                        renderEvents();
                        updateStatistics();
                        updateCharts();
                        updateRecentEvents();
                    } else if (Array.isArray(data)) {
                        events = data.map(event => ({
                            ...event,
                            category_name: event.category,
                            category_color: event.category_color
                        }));
                        renderEvents();
                        updateStatistics();
                        updateCharts();
                        updateRecentEvents();
                    } else {
                        console.warn('Неожиданный формат данных событий:', data);
                        loadTestEvents();
                    }
                })
                .catch(error => {
                    console.error(`Ошибка при загрузке событий из ${path}:`, error);
                    requestIndex++;
                    tryNextPath();
                });
        }
        
        tryNextPath();
    }
    
    function renderEvents() {
        console.log('Отрисовка событий, количество:', events.length);
        
        // Очищаем все события
        document.querySelectorAll('.plan-event, .fact-event').forEach(el => el.remove());
        
        if (events.length === 0) {
            console.log('Нет событий для отображения');
            return;
        }
        
        events.forEach((event, index) => {
            try {
                const start = new Date(event.start_time);
                const end = new Date(event.end_time);
                
                const startHour = start.getHours() + start.getMinutes() / 60;
                const endHour = end.getHours() + end.getMinutes() / 60;
                
                const duration = (endHour - startHour) * 4; // В слотах по 15 минут
                const startSlot = Math.round((startHour - START_HOUR) * 4);
                
                if (startSlot < 0 || startSlot >= scheduleBody.children.length) {
                    console.warn(`Событие вне диапазона времени: ${startHour}:00`);
                    return;
                }
                
                // Получаем день недели (0=воскресенье, 1=понедельник...6=суббота)
                const dayOfWeek = start.getDay();
                const adjustedDay = dayOfWeek === 0 ? 6 : dayOfWeek - 1; // Приводим к 0-6 (пн=0...вс=6)
                
                const row = scheduleBody.children[startSlot];
                if (!row) {
                    console.warn(`Не найдена строка для слота ${startSlot}`);
                    return;
                }
                
                const cell = row.children[adjustedDay + 1]; // +1 для колонки времени
                if (!cell) {
                    console.warn(`Не найдена ячейка для дня ${adjustedDay}`);
                    return;
                }
                
                const targetCell = event.type === 'plan' ? 
                    cell.querySelector('.plan-cell') : 
                    cell.querySelector('.fact-cell');
                
                if (!targetCell) {
                    console.warn(`Не найдена целевая ячейка для типа ${event.type}`);
                    return;
                }
                
                const eventDiv = document.createElement('div');
                eventDiv.className = event.type === 'plan' ? 'plan-event' : 'fact-event';
                eventDiv.textContent = event.category_name || event.category?.name || 'Без категории';
                
                // Форматируем время для tooltip
                const startTimeStr = start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                const endTimeStr = end.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                eventDiv.title = `${event.category_name || 'Без категории'}\n${startTimeStr} - ${endTimeStr}`;
                
                // Цвет категории
                eventDiv.style.borderLeftColor = event.category_color || 
                                                event.category?.color || 
                                                (event.type === 'plan' ? '#198754' : '#0d6efd');
                
                if (duration > 1) {
                    eventDiv.style.height = `calc(${duration * 40}px - 2px)`;
                    eventDiv.style.position = 'absolute';
                    eventDiv.style.top = '0';
                    eventDiv.style.left = '2px';
                    eventDiv.style.right = '2px';
                    eventDiv.style.zIndex = '1';
                }
                
                targetCell.appendChild(eventDiv);
                console.log(`Событие ${index} добавлено: ${event.category_name} в ${startTimeStr}`);
                
            } catch (error) {
                console.error(`Ошибка при отрисовке события ${index}:`, error, event);
            }
        });
    }
    
    // Новые функции для графиков и статистики
    
    function updateStatistics() {
        let planHours = 0;
        let factHours = 0;
        let todayPlanHours = 0;
        let todayFactHours = 0;
        
        const today = new Date().toDateString();
        
        events.forEach(event => {
            try {
                const start = new Date(event.start_time);
                const end = new Date(event.end_time);
                const duration = (end - start) / (1000 * 60 * 60); // Часы
                
                if (event.type === 'plan') {
                    planHours += duration;
                    if (start.toDateString() === today) {
                        todayPlanHours += duration;
                    }
                } else {
                    factHours += duration;
                    if (start.toDateString() === today) {
                        todayFactHours += duration;
                    }
                }
            } catch (error) {
                console.error('Ошибка при расчете статистики для события:', event, error);
            }
        });
        
        const todayPercentage = todayPlanHours > 0 ? 
            Math.round((todayFactHours / todayPlanHours) * 100) : 0;
        
        const weekPercentage = planHours > 0 ? 
            Math.round((factHours / planHours) * 100) : 0;
        
        // Обновляем статистику
        document.getElementById('todayPercentage').textContent = `${todayPercentage}%`;
        document.getElementById('weekPercentage').textContent = `${weekPercentage}%`;
        document.getElementById('totalHours').textContent = `${Math.round(factHours)}ч`;
        document.getElementById('totalEvents').textContent = events.length;
        
        console.log('Статистика обновлена:', { 
            todayPercentage, 
            weekPercentage, 
            totalHours: Math.round(factHours),
            totalEvents: events.length 
        });
    }
    
    function updateCharts() {
        // Простой график выполнения плана по дням
        updateWeeklyChart();
        
        // Распределение по категориям
        updateCategoryDistribution();
    }
    
    function updateWeeklyChart() {
        // Собираем данные по дням недели
        const daysData = {
            'Пн': { plan: 0, fact: 0 },
            'Вт': { plan: 0, fact: 0 },
            'Ср': { plan: 0, fact: 0 },
            'Чт': { plan: 0, fact: 0 },
            'Пт': { plan: 0, fact: 0 },
            'Сб': { plan: 0, fact: 0 },
            'Вс': { plan: 0, fact: 0 }
        };
        
        const dayNames = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
        
        events.forEach(event => {
            try {
                const start = new Date(event.start_time);
                const end = new Date(event.end_time);
                const duration = (end - start) / (1000 * 60 * 60); // Часы
                const dayName = dayNames[start.getDay()];
                
                if (event.type === 'plan') {
                    daysData[dayName].plan += duration;
                } else {
                    daysData[dayName].fact += duration;
                }
            } catch (error) {
                console.error('Ошибка при обработке события для графика:', error);
            }
        });
        
        // Создаем простой текстовый график
        let chartHTML = '<div class="mt-3">';
        Object.entries(daysData).forEach(([day, data]) => {
            const total = data.plan + data.fact;
            const percentage = data.plan > 0 ? Math.round((data.fact / data.plan) * 100) : 0;
            
            chartHTML += `
                <div class="mb-3">
                    <div class="d-flex justify-content-between mb-1">
                        <span class="small">${day}</span>
                        <span class="small">${percentage}%</span>
                    </div>
                    <div class="progress" style="height: 20px;">
                        <div class="progress-bar bg-success" role="progressbar" 
                             style="width: ${percentage}%" 
                             title="План: ${Math.round(data.plan)}ч, Факт: ${Math.round(data.fact)}ч">
                            ${Math.round(data.fact)}ч
                        </div>
                    </div>
                    <div class="d-flex justify-content-between mt-1">
                        <small class="text-muted">План: ${Math.round(data.plan)}ч</small>
                        <small class="text-muted">Факт: ${Math.round(data.fact)}ч</small>
                    </div>
                </div>
            `;
        });
        chartHTML += '</div>';
        
        weeklyChart.innerHTML = chartHTML;
    }
    
    function updateCategoryDistribution() {
        // Считаем время по категориям
        const categoryStats = {};
        
        events.forEach(event => {
            try {
                const start = new Date(event.start_time);
                const end = new Date(event.end_time);
                const duration = (end - start) / (1000 * 60 * 60); // Часы
                
                const categoryName = event.category_name || 'Без категории';
                const categoryColor = event.category_color || '#6c757d';
                
                if (!categoryStats[categoryName]) {
                    categoryStats[categoryName] = {
                        hours: 0,
                        color: categoryColor,
                        count: 0
                    };
                }
                
                categoryStats[categoryName].hours += duration;
                categoryStats[categoryName].count += 1;
            } catch (error) {
                console.error('Ошибка при обработке события для распределения:', error);
            }
        });
        
        // Сортируем по убыванию часов
        const sortedCategories = Object.entries(categoryStats)
            .sort((a, b) => b[1].hours - a[1].hours);
        
        // Считаем общее время для процентного расчета
        const totalHours = sortedCategories.reduce((sum, [_, stat]) => sum + stat.hours, 0);
        
        // Создаем визуализацию
        let distributionHTML = '';
        
        if (sortedCategories.length === 0) {
            distributionHTML = `
                <div class="text-center py-4 text-muted">
                    <i class="bi bi-pie-chart" style="font-size: 2rem; opacity: 0.3;"></i>
                    <p class="mt-2">Нет данных для отображения</p>
                </div>
            `;
        } else {
            sortedCategories.forEach(([categoryName, stat]) => {
                const percentage = totalHours > 0 ? Math.round((stat.hours / totalHours) * 100) : 0;
                
                distributionHTML += `
                    <div class="category-item">
                        <div>
                            <div class="d-flex align-items-center">
                                <span class="category-color" style="background-color: ${stat.color};"></span>
                                <strong>${categoryName}</strong>
                            </div>
                            <small class="text-muted">${stat.count} событий, ${Math.round(stat.hours)} часов</small>
                        </div>
                        <div class="text-end">
                            <div class="fw-bold">${percentage}%</div>
                        </div>
                    </div>
                    <div class="category-bar" style="width: ${percentage}%; background-color: ${stat.color};"></div>
                `;
            });
        }
        
        categoryDistribution.innerHTML = distributionHTML;
    }
    
    function updateRecentEvents() {
        // Берем последние 5 событий
        const recent = events
            .sort((a, b) => new Date(b.start_time) - new Date(a.start_time))
            .slice(0, 5);
        
        let eventsHTML = '';
        
        if (recent.length === 0) {
            eventsHTML = `
                <div class="text-muted text-center py-2">
                    <small>Нет последних событий</small>
                </div>
            `;
        } else {
            recent.forEach(event => {
                try {
                    const start = new Date(event.start_time);
                    const end = new Date(event.end_time);
                    const startTimeStr = start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                    const endTimeStr = end.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                    const dateStr = start.toLocaleDateString('ru-RU', { 
                        day: 'numeric', 
                        month: 'short' 
                    });
                    
                    eventsHTML += `
                        <div class="d-flex justify-content-between align-items-center mb-2 p-2 border rounded">
                            <div>
                                <div class="d-flex align-items-center">
                                    <span class="category-color" style="background-color: ${event.category_color || '#6c757d'};"></span>
                                    <small class="fw-bold">${event.category_name || 'Без категории'}</small>
                                </div>
                                <div class="small text-muted">
                                    ${dateStr}, ${startTimeStr}-${endTimeStr}
                                </div>
                            </div>
                            <span class="badge ${event.type === 'plan' ? 'bg-success' : 'bg-primary'}">
                                ${event.type === 'plan' ? 'План' : 'Факт'}
                            </span>
                        </div>
                    `;
                } catch (error) {
                    console.error('Ошибка при отображении последнего события:', error);
                }
            });
        }
        
        recentEvents.innerHTML = eventsHTML;
    }
    
    // Остальные функции (initColorPicker, initTimeSelects, initModalDates, тестовые данные)
    // ... оставляем без изменений, как в предыдущем коде
    
    // Обработчики событий для кнопок навигации недели
    weekPicker.addEventListener('change', function() {
        console.log('Неделя изменена:', weekPicker.value);
        loadEvents();
    });
    
    currentWeekBtn.addEventListener('click', function() {
        const today = new Date();
        const firstDayOfYear = new Date(today.getFullYear(), 0, 1);
        const pastDaysOfYear = (today - firstDayOfYear) / 86400000;
        const weekNumber = Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7);
        const currentWeek = `${today.getFullYear()}-W${weekNumber.toString().padStart(2, '0')}`;
        
        weekPicker.value = currentWeek;
        console.log('Переход к текущей неделе:', currentWeek);
        loadEvents();
    });
    
    prevWeekBtn.addEventListener('click', function() {
        const [year, week] = weekPicker.value.split('-W');
        let newWeek = parseInt(week) - 1;
        let newYear = parseInt(year);
        
        if (newWeek < 1) {
            newYear--;
            newWeek = 52;
        }
        
        weekPicker.value = `${newYear}-W${newWeek.toString().padStart(2, '0')}`;
        console.log('Предыдущая неделя:', weekPicker.value);
        loadEvents();
    });
    
    nextWeekBtn.addEventListener('click', function() {
        const [year, week] = weekPicker.value.split('-W');
        let newWeek = parseInt(week) + 1;
        let newYear = parseInt(year);
        
        if (newWeek > 52) {
            newYear++;
            newWeek = 1;
        }
        
        weekPicker.value = `${newYear}-W${newWeek.toString().padStart(2, '0')}`;
        console.log('Следующая неделя:', weekPicker.value);
        loadEvents();
    });
    
    // Обработчики для новых кнопок
    copyWeekBtn.addEventListener('click', function() {
        if (confirm('Скопировать план текущей недели на следующую неделю?')) {
            console.log('Копирование недели:', weekPicker.value);
            alert('Функция копирования недели временно недоступна');
        }
    });
    
    addCategoryBtn.addEventListener('click', function() {
        console.log('Открытие модального окна создания категории');
        const modal = new bootstrap.Modal(document.getElementById('categoryModal'));
        modal.show();
    });
    
    exportDataBtn.addEventListener('click', function() {
        console.log('Экспорт данных');
        alert('Функция экспорта данных временно недоступна');
    });
    
    // Инициализация завершена
    console.log('Страница расписания с графиками загружена');
});
</script>
{% endblock %}
