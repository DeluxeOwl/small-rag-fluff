from openai import OpenAI

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)


def create_query_message(context: str, question: str) -> str:
    template = f"""
    Context:
    {context}

    QUESTION:
    Based ONLY on the context above I've provided you, here is my question: 
    {question}
    """

    return template


chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Complete the json the sentence"},
    ],
)

print(chat_completion.choices[0].message)
