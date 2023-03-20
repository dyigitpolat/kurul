from chat_history.chat_history import ChatHistory

import openai
import backoff

@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_tries=10)
def completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

class OpenAIClient:
    def __init__(self, model="gpt-3.5-turbo"):
        self.chat_history = ChatHistory()
        self.model = model

    def respond(self, text):
        self.chat_history.append({"role": "user", "content": text})
        try:
            response = completions_with_backoff(
                model=self.model,
                messages=list(self.chat_history.messages),
                timeout=15
            ).choices[0].message

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
            return "No response."

    