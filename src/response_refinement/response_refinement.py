from language_model_handling.gpt4_client import GPT4Client
from prompts.prompts import Prompts

class ResponseRefinement:
    def __init__(self):
        pass

    def refine(self, chat_history, skepticism):
        refinement_prompt = Prompts.skepticism_refinement_prompt
        assistant = GPT4Client()

        prompt_for_assistant = "--\n\n"
        prompt_for_assistant += chat_history.to_text()
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += skepticism
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += refinement_prompt

        response = assistant.respond(prompt_for_assistant)
        return response