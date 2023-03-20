from context_management.context_manager import ContextManager
from language_model_handling.openai_client import OpenAIClient
from skeptical_prompt_generation.simple_skepticism import SimpleSkepticism
from response_refinement.response_refinement import ResponseRefinement
from input_processing.input_processing import InputProcessor
from output_processing.output_processing import OutputProcessor
from chat_history.chat_history import ChatHistory
from prompts.prompts import Prompts

class Kurul:
    def __init__(self):
        self.first_assistant = OpenAIClient()
        # self.first_assistant.respond(Prompts.pre_prompt)

        self.context_manager = ContextManager([self.first_assistant.chat_history])

    def respond(self, text):
        text = InputProcessor().process(text)
        self.first_assistant.respond(text)

        response_history = ChatHistory(self.first_assistant.chat_history.messages[-2:])
        response_history_text = response_history.to_text().replace("user:::", "A:").replace("assistant:::", "B:")

        skeptical_assistant = OpenAIClient()
        skeptic_query = \
            "Summary:\n" + \
            self.context_manager.context_summary + \
            "\n\n--\n\n" + \
            response_history_text + \
            "\n\n--\n\n" + SimpleSkepticism().generate_skeptical_prompt()
        
        skepticism = skeptical_assistant.respond(skeptic_query)

        refined_response = ResponseRefinement().refine(self.context_manager.context_summary, response_history, skepticism)
        self.first_assistant.chat_history[-1]["content"] = refined_response

        self.context_manager.update()
        return OutputProcessor().process(refined_response)