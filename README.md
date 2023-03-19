# kurul

kurul leverages the power of OpenAI GPT-4 to provide high-quality responses in a friendly and interactive manner. kurul refines its responses using a pipeline of skepticism to ensure relevant and thoughtful conversations with users.

kurul can be interacted thorugh a Telegram bot.

## Dependencies

- Python 3.10
- python-telegram-bot
- openai python package

## Setup

1. Clone the repository.

```
git clone https://github.com/dyigitpolat/kurul.git
```

2. Install the required packages.

```
pip install python-telegram-bot openai
```

3. Configure the API keys and authorized chats.

- Obtain an API key from the [OpenAI](https://beta.openai.com/signup/) platform after signing up for a free account.

- Replace the placeholders in the `src/api_keys.py` file with your OpenAI API key and Telegram bot token. For example:

```python
openai_api_key = "your_openai_key_here"
telegram_bot_api_key = "your_telegram_bot_token_here"
```

- To add authorized users, you need to find their Telegram chat ID. Add the Telegram chat IDs of authorized users to the `src/authorized_chats.py` file. For example:

```python
authorized_chat_ids = [
    123456789, # UserID 1
    987654321, # UserID 2
]
```

4. Set up a Telegram bot by following [this guide](https://core.telegram.org/bots#6-botfather) from the official Telegram documentation.

## Usage

```
cd src
python main.py
```

The chatbot will automatically respond to messages sent by authorized users on the Telegram platform.

## Architecture Overview

kurul's core functionality is encapsulated in the `kurul` class. It uses a pipeline of skepticism to improve the quality of GPT-4 responses. Main components include:

- GPT-4 client for initial response generation
- Context manager for handling conversations context
- Skeptical prompt generation for creating skepticism queries
- Response refinement based on the skepticism feedback

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for more information.

## Contributing

Contributions are welcome! Feel free to submit a pull request, report a bug, or suggest new features by creating an issue.

Please make sure to update tests as appropriate and follow the existing coding style.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the Telegram integration.
- [OpenAI](https://openai.com/) for the GPT-4 API.