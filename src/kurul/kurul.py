from language_model_handling.gpt4_client import GPT4Client

class Kurul:
    def __init__(self):
        self.first_assistant = GPT4Client()

    def respond(self, text):
        return self.first_assistant.respond(text)