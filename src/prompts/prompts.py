class Prompts:
    conversation_distillation_prompt = "Write a concise version of the conversation above in the same conversation format. Retain the key points. Use assistant::: and user::: to indicate who is speaking."
    conversation_summary_prompt_f = "Summarize the context of the conversation(s) {}"
    skepticism_refinement_prompt = "Improve and elaborate B's response based on analyst's feedback. Provide the improved and elaborated response between [[[ ]]]"
    simple_skepticism_prompt = "Explain the major problems with the answer: "
    helpful_character_prompt = "a very helpful expert person"
    pre_prompt = """
From now on, you are going to generate responses to my messages as if they are from {0}. 
The responses must build upon the conversation history and must introduce new ideas. 
The responses should reflect the characteristics of {0}. 
Use emojis. Only one reponse at a time.

--

Hello!
    """.format(helpful_character_prompt)
