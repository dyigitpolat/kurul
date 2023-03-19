class Prompts:
    conversation_distillation_prompt = "Write a concise version of the conversation above in the same conversation format. Retain the key points. Use assistant::: and user::: to indicate who is speaking."
    conversation_summary_prompt_f = "Summarize the context of the conversation(s) {}"
    skepticism_refinement_prompt = "Rewrite the improved version of assistant's response based on analyst's feedback. Retain the structure."
    simple_skepticism_prompt = "Explain the major problems with the answer: "
