# Hackathon Group 1: Discord Bot

A simple Discord bot that Group 1 built during a March 2024 hackathon. It was also a first hands-on exercise with Git branches and pull requests.

## What it does

- Logs in and prints the bot's username when it's ready
- Replies to any message that starts with `hello`:
  > Hello @you! I am a basic Discord bot.
- Ignores its own messages

## Setup

1. Create an application and bot at the [Discord Developer Portal](https://discord.com/developers/applications), turn on the **Message Content** and **Server Members** intents, and copy the bot token.
2. Install the dependency:
   ```bash
   pip install discord.py
   ```
3. Provide the token through an environment variable. **Never commit it.**
   ```bash
   export TOKEN="your-bot-token"
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

## Files

| File | Purpose |
|---|---|
| `main.py` | The bot |
| `gitCheatSheet.txt` | Git commands the group collected while learning branching and PRs |
