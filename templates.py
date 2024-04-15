def create_query_message(context: str, question: str) -> str:
    template = f"""
    Context:
    {context}

    QUESTION:
    Based ONLY on the context above I've provided you, here is my question (respond in two sentences, and finish with a joke, with emoji only): 
    {question}
    """

    return template
