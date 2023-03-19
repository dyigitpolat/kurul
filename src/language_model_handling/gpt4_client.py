from chat_history.chat_history import ChatHistory

import openai

class GPT4Client:
    def __init__(self):
        self.chat_history = ChatHistory()

    def respond(self, text):
        self.chat_history.append({"role": "user", "content": text})

        self.chat_history.append(
            openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.chat_history.messages
            ).choices[0].message)

        print("Query:", text)
        print("Response:", self.chat_history[-1].content)
        return self.chat_history[-1].content

    