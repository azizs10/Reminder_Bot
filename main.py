import asyncio
import re
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, F 
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = 'Your_Bot_Token_Here'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
user_t = {} 

@dp.message(Command("start"))
async def cmd_s(message: Message):
    await message.answer(
        "Hi! I'm your productivity bot.\n\n"
        "Here's what I can do:\n"
        "1. Just text me to add a task (default reminder in 1 hour).\n"
        "2. Type 'remove [task text]' or 'delete [task text]' to delete it.\n"
        "3. Include 'at HH:MM' in your text to set a specific reminder time (e.g., 'Buy milk at 15:30').\n\n"
        "The /tasks command shows the to-do list.\n"
        "The /clear command clears your to-do list."
    )

@dp.message(Command("tasks"))
async def s_t(message: Message):
    user_id = message.from_user.id
    tasks = user_t.get(user_id, [])
    if not tasks:
        await message.answer('Your to-do list is empty! Are you relaxing?')
        return

    text = "Your tasks for today:\n"
    for i, task in enumerate(tasks, start=1):
        text += f"{i}. {task}\n"
    await message.answer(text)

@dp.message(Command("clear"))
async def clear_t(message: Message):
    user_id = message.from_user.id 
    user_t[user_id] = []
    await message.answer("Task list successfully cleared!")

@dp.message(F.text)
async def handle_text(message: Message):
    user_id = message.from_user.id 
    text_input = message.text
    text_lower = text_input.lower()

    if user_id not in user_t:
        user_t[user_id] = []

    if text_lower.startswith("remove ") or text_lower.startswith("delete "):
        task_to_remove = text_input.split(maxsplit=1)[1]
        found_task = None
        for task in user_t[user_id]:
            if task.lower() == task_to_remove.lower():
                found_task = task
                break
                
        if found_task:
            user_t[user_id].remove(found_task)
            await message.answer("Success! Task removed.")
        else:
            await message.answer("Task not found in your list.")
        return

    time_match = re.search(r'\bat\s+(\d{1,2})[:.](\d{2})\b', text_lower)
    delay = 3600

    if time_match:
        hours = int(time_match.group(1))
        minutes = int(time_match.group(2))
        now = datetime.now()
        target_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
        if target_time < now:
            target_time += timedelta(days=1)
        delay = (target_time - now).total_seconds()
        await message.answer(f"Success! Specific reminder set for {hours:02d}:{minutes:02d}.")
    else:
        await message.answer("Success!")

    user_t[user_id].append(text_input)

    async def remind(task_text: str, sleep_time: float):
        await asyncio.sleep(sleep_time)
        if user_id in user_t and task_text in user_t[user_id]:
            await message.answer(f"Reminder: Don't forget to do \"{task_text}\"!")
            
    asyncio.create_task(remind(text_input, delay))

async def main():
    print("Bot launched and ready to work...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())