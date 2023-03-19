import openai

class GPT4Client:
    def __init__(self):
        self.message_history = []

    def respond(self, text):
        self.message_history.append({"role": "user", "content": text})

        self.message_history.append(
            openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.message_history).choices[0].message)

        return self.message_history[-1].content

    