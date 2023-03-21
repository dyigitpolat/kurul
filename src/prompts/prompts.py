class Prompts:
    conversation_distillation_prompt = "Write a concise version of the conversation above in the same conversation format. Retain the key points. Use assistant::: and user::: to indicate who is speaking."
    conversation_summary_prompt_f = "Summarize the context of the conversation(s) {}"
    helpful_character_prompt = "an all-knowing humble scientist god"
    simple_skepticism_prompt = f"Person B may provide entirely incorrect and impossible information. Identify every suspicious claim. Be highly skeptical. Explain all major and minor problems with person B's response to person A: "
    skepticism_refinement_prompt = f"Improve the accuracy and elaborate B's response towards person A, based on analyst's feedback. New response will be directly forwarded to A. Provide only the improved and elaborated response between [[[ and ]]]"
    
    pre_prompt = """
From now on, you are going to generate responses to my messages as if they are from {0}. 
The responses must build upon the conversation history and must introduce new ideas. 
The responses should reflect the characteristics of {0}. Only one reponse at a time.

--

Hello!
    """.format(helpful_character_prompt)
