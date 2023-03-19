from chat_history.chat_history import ChatHistory

import openai
import time

class OpenAIClient:
    def __init__(self, model="gpt-4"):
        self.chat_history = ChatHistory()
        self.model = model

    def respond(self, text):
        self.chat_history.append({"role": "user", "content": text})
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=list(self.chat_history.messages)
            ).choices[0].message
            time.sleep(2)

            print("\n---------\n")
            print("Query:", text)
            print("Response:", response.content)
            print("\n---------\n")
            self.chat_history.append(response)

            return response.content
        
        except Exception as e:
            print("\n---------\n")
            print(f"Error: {e}")
            print("\n---------\n")
            return "I am having internal issues. Please try again."

    