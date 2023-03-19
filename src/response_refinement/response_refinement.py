from language_model_handling.openai_client import OpenAIClient
from prompts.prompts import Prompts

class ResponseRefinement:
    def __init__(self):
        pass

    def refine(self, chat_history, skepticism):
        refinement_prompt = Prompts.skepticism_refinement_prompt
        assistant = OpenAIClient()

        prompt_for_assistant = "\n\n--\n\n"
        prompt_for_assistant += chat_history.to_text()
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += "Analyst:\n"
        prompt_for_assistant += skepticism
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += refinement_prompt

        response = assistant.respond(prompt_for_assistant)
        return response