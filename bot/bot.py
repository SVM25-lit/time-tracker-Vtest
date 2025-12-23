import os
import requests
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Конфигурация
API_URL = os.environ.get('API_URL', 'https://time-tracker-z6co.onrender.com/api/v1')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def get_user_categories(user_id):
    """Получить категории пользователя"""
    response = requests.get(
        f'{API_URL}/telegram/categories',
        headers={'X-Telegram-ID': str(user_id)},
        timeout=10
    )
    
    if response.status_code == 200:
        return response.json()['categories']
    return []


def create_event(user_id, category_id, start_time, end_time):
    """Создать событие в БД"""
    try:
        response = requests.post(
            f'{API_URL}/telegram/events',
            headers={'X-Telegram-ID': str(user_id)},
            json={
                'category_id': category_id,
                'time': f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}",
                'type': 'fact'
            },
            timeout=10
        )
        return response.status_code == 201
    except Exception as e:
        logger.error(f"Error creating event: {e}")
        return False


def finish_current_activity(user_data, user_id):
    """Завершить текущую активность и записать в БД"""
    if 'current_category' in user_data and 'start_time' in user_data:
        category_id = user_data['current_category']
        start_time = user_data['start_time']
        end_time = datetime.now()
        
        # Создаем событие
        success = create_event(user_id, category_id, start_time, end_time)
        
        # Очищаем текущую активность
        category_name = user_data.get('category_name', 'Неизвестно')
        user_data.pop('current_category', None)
        user_data.pop('category_name', None)
        user_data.pop('start_time', None)
        
        duration = end_time - start_time
        hours = int(duration.total_seconds() // 3600)
        minutes = int((duration.total_seconds() % 3600) // 60)
        
        return {
            'success': success,
            'category': category_name,
            'duration': f"{hours}ч {minutes}м",
            'start': start_time.strftime('%H:%M'),
            'end': end_time.strftime('%H:%M')
        }
    return None


# ========== ОСНОВНЫЕ ОБРАБОТЧИКИ ==========

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    
    # Проверяем/регистрируем пользователя в системе
    response = requests.post(f'{API_URL}/telegram/auth', 
                           json={'telegram_id': str(user.id), 'username': user.username or user.first_name},
                           timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['status'] == 'authenticated':
            # Проверяем, есть ли активность
            current_category = context.user_data.get('current_category')
            
            if current_category:
                # Показываем статус текущей активности
                category_name = context.user_data.get('category_name', 'Неизвестно')
                start_time = context.user_data.get('start_time', datetime.now())
                duration = datetime.now() - start_time
                hours = int(duration.total_seconds() // 3600)
                minutes = int((duration.total_seconds() % 3600) // 60)
                
                keyboard = [
                    [InlineKeyboardButton("⏹️ Завершить активность", callback_data='stop_activity')],
                    [InlineKeyboardButton("🔄 Сменить категорию", callback_data='switch_category')],
                    [InlineKeyboardButton("📊 Статистика", callback_data='stats')],
                    [InlineKeyboardButton("🏷️ Мои категории", callback_data='categories')],
                ]
                
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await update.message.reply_text(
                    f'Привет, {user.first_name}! 👋\n'
                    f'Вы авторизованы как {data["username"]}\n\n'
                    f'📌 Сейчас активна категория: **{category_name}**\n'
                    f'⏱️ Длительность: {hours}ч {minutes}м\n'
                    f'🕐 Начало: {start_time.strftime("%H:%M")}\n\n'
                    f'Что вы хотите сделать?',
                    reply_markup=reply_markup,
                    parse_mode='Markdown'
                )
            else:
                # Нет активной категории - показываем обычное меню
                keyboard = [
                    [InlineKeyboardButton("▶️ Начать активность", callback_data='start_activity')],
                    [InlineKeyboardButton("📊 Статистика", callback_data='stats')],
                    [InlineKeyboardButton("🏷️ Мои категории", callback_data='categories')],
                ]
                
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await update.message.reply_text(
                    f'Привет, {user.first_name}! 👋\n'
                    f'Вы авторизованы как {data["username"]}\n'
                    'Выберите действие:',
                    reply_markup=reply_markup
                )
        else:
            await update.message.reply_text(
                'Для использования бота необходимо сначала зарегистрироваться '
                'через веб-интерфейс:\n'
                f'{data["registration_url"]}'
            )
    else:
        await update.message.reply_text('Ошибка подключения к серверу. Попробуйте позже.')


async def start_activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начать выбор категории для новой активности"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    categories = get_user_categories(user_id)
    
    if not categories:
        await query.edit_message_text('У вас нет категорий. Сначала создайте их в веб-интерфейсе.')
        return
    
    # Создаем клавиатуру с категориями
    keyboard = []
    row = []
    for i, cat in enumerate(categories):
        row.append(InlineKeyboardButton(cat['name'], callback_data=f'cat_{cat["id"]}'))
        if (i + 1) % 2 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton("↩️ Назад", callback_data='back_to_main')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        'Выберите категорию для начала активности:',
        reply_markup=reply_markup
    )


async def category_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик выбора категории"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    # Извлекаем ID категории
    category_id = int(query.data.replace('cat_', ''))
    
    # Получаем все категории чтобы найти имя
    categories = get_user_categories(user_id)
    category_name = next((cat['name'] for cat in categories if cat['id'] == category_id), "Неизвестно")
    
    # Завершаем предыдущую активность (если есть)
    result = finish_current_activity(context.user_data, user_id)
    
    # Начинаем новую активность
    context.user_data['current_category'] = category_id
    context.user_data['category_name'] = category_name
    context.user_data['start_time'] = datetime.now()
    
    # Сообщаем пользователю
    if result:
        await query.edit_message_text(
            f'✅ **{result["category"]}** завершена: {result["duration"]} ({result["start"]}-{result["end"]})\n'
            f'▶️ Начинаю отсчет для **{category_name}**...',
            parse_mode='Markdown'
        )
    else:
        await query.edit_message_text(
            f'▶️ Начинаю отсчет для **{category_name}**...',
            parse_mode='Markdown'
        )
    
    # Показываем меню управления
    keyboard = [
        [InlineKeyboardButton("⏹️ Завершить", callback_data='stop_activity')],
        [InlineKeyboardButton("🔄 Сменить категорию", callback_data='switch_category')],
        [InlineKeyboardButton("📊 Статистика", callback_data='stats')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        f'Категория **{category_name}** активна. Что дальше?',
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def stop_activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Завершить текущую активность"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    result = finish_current_activity(context.user_data, user_id)
    
    if result:
        await query.edit_message_text(
            f'✅ **{result["category"]}** завершена!\n'
            f'⏱️ Длительность: {result["duration"]}\n'
            f'🕐 Время: {result["start"]}-{result["end"]}',
            parse_mode='Markdown'
        )
    else:
        await query.edit_message_text('❌ Нет активной категории для завершения.')


async def switch_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сменить категорию (завершить текущую и начать выбор новой)"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    # Завершаем текущую активность
    result = finish_current_activity(context.user_data, user_id)
    
    if result:
        await query.edit_message_text(
            f'✅ **{result["category"]}** завершена: {result["duration"]}\n'
            f'Теперь выберите новую категорию:',
            parse_mode='Markdown'
        )
    else:
        await query.edit_message_text('Выберите новую категорию:')
    
    # Показываем выбор категорий
    await start_activity(update, context)


async def text_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений (для быстрого переключения по названию)"""
    message_text = update.message.text.strip()
    user_id = update.effective_user.id
    
    # Команда "стоп" или "stop"
    if message_text.lower() in ['стоп', 'stop', 'завершить']:
        result = finish_current_activity(context.user_data, user_id)
        
        if result:
            await update.message.reply_text(
                f'✅ **{result["category"]}** завершена!\n'
                f'⏱️ Длительность: {result["duration"]}\n'
                f'🕐 Время: {result["start"]}-{result["end"]}',
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text('❌ Нет активной категории для завершения.')
        return
    
    # Ищем категорию по названию
    categories = get_user_categories(user_id)
    
    # Ищем точное совпадение
    found_category = None
    for cat in categories:
        if cat['name'].lower() == message_text.lower():
            found_category = cat
            break
    
    # Ищем частичное совпадение
    if not found_category:
        for cat in categories:
            if message_text.lower() in cat['name'].lower():
                found_category = cat
                break
    
    if found_category:
        # Завершаем предыдущую активность
        result = finish_current_activity(context.user_data, user_id)
        
        # Начинаем новую
        context.user_data['current_category'] = found_category['id']
        context.user_data['category_name'] = found_category['name']
        context.user_data['start_time'] = datetime.now()
        
        if result:
            await update.message.reply_text(
                f'✅ **{result["category"]}** завершена: {result["duration"]}\n'
                f'▶️ Начинаю отсчет для **{found_category["name"]}**...',
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                f'▶️ Начинаю отсчет для **{found_category["name"]}**...',
                parse_mode='Markdown'
            )
    else:
        await update.message.reply_text(
            'Категория не найдена. Доступные команды:\n'
            '• Название категории - начать/сменить активность\n'
            '• "стоп" - завершить текущую активность\n'
            '• /start - главное меню\n'
            '• /stats - статистика'
        )


async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик статистики"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    try:
        response = requests.get(
            f'{API_URL}/telegram/stats',
            headers={'X-Telegram-ID': str(user_id)},
            timeout=10
        )
        
        if response.status_code == 200:
            stats = response.json()
            message = (
                f'📊 **Ваша статистика**\n\n'
                f'• Событий сегодня: {stats["today"]}\n'
                f'• Всего событий: {stats["total"]}\n'
                f'• Запланировано: {stats["plan"]}\n'
                f'• Выполнено: {stats["fact"]}\n'
                f'• Выполнение: {stats["completion_rate"]}%\n\n'
                f'{stats["message"]}'
            )
            await query.edit_message_text(message, parse_mode='Markdown')
        else:
            await query.edit_message_text('Не удалось получить статистику. Ошибка сервера.')
    except Exception as e:
        logging.error(f"Error getting stats: {e}")
        await query.edit_message_text('Ошибка подключения к серверу статистики.')


async def categories_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать категории пользователя"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    categories = get_user_categories(user_id)
    
    if not categories:
        await query.edit_message_text('У вас нет категорий. Создайте их в веб-интерфейсе.')
        return
    
    categories_list = '\n'.join([f'• {cat["name"]}' for cat in categories])
    
    await query.edit_message_text(
        f'🏷️ **Ваши категории:**\n\n{categories_list}\n\n'
        f'Используйте название категории для быстрого переключения.',
        parse_mode='Markdown'
    )


async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Вернуться в главное меню"""
    query = update.callback_query
    await query.answer()
    
    await start(Update(message=query.message, effective_user=query.from_user), context)


def main():
    """Запуск бота"""
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", stats_handler))
    
    # Обработчики callback-запросов
    application.add_handler(CallbackQueryHandler(start_activity, pattern='^start_activity$'))
    application.add_handler(CallbackQueryHandler(stop_activity, pattern='^stop_activity$'))
    application.add_handler(CallbackQueryHandler(switch_category, pattern='^switch_category$'))
    application.add_handler(CallbackQueryHandler(stats_handler, pattern='^stats$'))
    application.add_handler(CallbackQueryHandler(categories_handler, pattern='^categories$'))
    application.add_handler(CallbackQueryHandler(back_to_main, pattern='^back_to_main$'))
    application.add_handler(CallbackQueryHandler(category_chosen, pattern='^cat_'))
    
    # Обработчик текстовых сообщений (для быстрого переключения по названию)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message_handler))
    
    # Запуск бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
