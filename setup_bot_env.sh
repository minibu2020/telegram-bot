#!/bin/bash

# Name of the virtual environment directory
VENV_DIR="telegram-bot-env"

# Your bot script filename
BOT_SCRIPT="group_welcome_bot.py"

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv $VENV_DIR
fi

# Step 2: Activate the virtual environment
echo "🚀 Activating virtual environment..."
source $VENV_DIR/bin/activate

# Step 3: Install dependencies
echo "📚 Installing python-telegram-bot..."
pip install --upgrade pip
pip install python-telegram-bot

# Step 4: Optional - run your bot
if [ -f "$BOT_SCRIPT" ]; then
  echo "▶️ Running your bot: $BOT_SCRIPT"
  python $BOT_SCRIPT
else
  echo "⚠️ Bot script '$BOT_SCRIPT' not found. You can run it later with:"
  echo "   source $VENV_DIR/bin/activate && python your_bot.py"
fi
