# 🎯 Productivity Telegram Bot

An asynchronous Telegram bot designed to supercharge your personal daily productivity. Built with Python and the modern **aiogram 3.x** framework, this bot helps you effortlessly capture tasks and manage your daily to-do list right within Telegram.

## 🚀 Features

- **Quick Task Capture:** Simply send any text message to the bot, and it instantly adds it to your daily tasks.
- **Task Management:** View your structured list with `/tasks` and wipe it clean with `/clear`.
- **Asynchronous & Fast:** Built entirely on top of `asyncio` for maximum performance and responsiveness.
- **Ready for Extensions:** Clean architecture that can easily be expanded with databases (SQLite/PostgreSQL) or scheduling engines (`apscheduler`).

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Framework:** `aiogram` (v3.x)
- **Concurrency:** `asyncio`

## ⚙️ Installation & Setup

Follow these steps to get your own instance of the bot running:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/productivity-telegram-bot.git
cd productivity-telegram-bot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install aiogram
```

### 4. Configure Your Bot Token
1. Message [@BotFather](https://t.me/BotFather) on Telegram and create a new bot using `/newbot`.
2. Copy your HTTP API token.
3. Open `bot.py` and replace `'Your_Bot_Token_Here'` with your actual token string (or set it via environment variables).

### 5. Run the Bot
```bash
python bot.py
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
