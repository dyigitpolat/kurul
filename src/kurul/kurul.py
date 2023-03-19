from context_management.context_manager import ContextManager
from language_model_handling.openai_client import OpenAIClient
from skeptical_prompt_generation.simple_skepticism import SimpleSkepticism
from response_refinement.response_refinement import ResponseRefinement

class Kurul:
    def __init__(self):
        self.first_assistant = OpenAIClient()
        self.context_manager = ContextManager([self.first_assistant.chat_history])

    def respond(self, text):
        skeptical_assistant = OpenAIClient()

        self.first_assistant.respond(text)
        skeptic_query = \
            self.context_manager.context_summary + ":\n\n" + \
            self.first_assistant.chat_history.to_text() + \
            "\n\n" + SimpleSkepticism().generate_skeptical_prompt()
        
        skepticism = skeptical_assistant.respond(skeptic_query)

        refined_response = ResponseRefinement().refine(self.first_assistant.chat_history, skepticism)
        self.context_manager.update()
        
        return refined_response