from language_model_handling.openai_client import OpenAIClient
from prompts.prompts import Prompts

class ResponseRefinement:
    def __init__(self):
        pass

    def refine(self, context_summary, chat_history, skepticism):
        refinement_prompt = Prompts.skepticism_refinement_prompt
        assistant = OpenAIClient()

        prompt_for_assistant = "Summary:\n"
        prompt_for_assistant += context_summary
        prompt_for_assistant = "\n\n--\n\n"
        prompt_for_assistant += chat_history.to_text().replace("user:::", "A:").replace("assistant:::", "B:")
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += "Analyst:\n"
        prompt_for_assistant += skepticism
        prompt_for_assistant += "\n\n--\n\n"
        prompt_for_assistant += refinement_prompt

        response = assistant.respond(prompt_for_assistant)
        response = response[response.find("[[[")+3:response.rfind("]]]")]
        return response