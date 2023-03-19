from context_management.context_manager import ContextManager
from language_model_handling.openai_client import OpenAIClient
from skeptical_prompt_generation.simple_skepticism import SimpleSkepticism
from response_refinement.response_refinement import ResponseRefinement
from input_processing.input_processing import InputProcessor
from output_processing.output_processing import OutputProcessor
from prompts.prompts import Prompts

class Kurul:
    def __init__(self):
        self.first_assistant = OpenAIClient()
        # self.first_assistant.respond(Prompts.pre_prompt)

        self.context_manager = ContextManager([self.first_assistant.chat_history])

    def respond(self, text):
        skeptical_assistant = OpenAIClient()

        text = InputProcessor().process(text)
        self.first_assistant.respond(text)
        skeptic_query = \
            self.context_manager.context_summary + ":\n\n" + \
            self.first_assistant.chat_history.to_text().replace("user:::", "A:").replace("assistant:::", "B:") + \
            "\n\n" + SimpleSkepticism().generate_skeptical_prompt()
        
        skepticism = skeptical_assistant.respond(skeptic_query)

        refined_response = ResponseRefinement().refine(self.first_assistant.chat_history, skepticism)
        self.first_assistant.chat_history[-1]["content"] = refined_response

        self.context_manager.update()
        return OutputProcessor().process(refined_response)