def build_prompt(context, history, question):

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['message']}\n"

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, say:
"I could not find the answer in the knowledge base."

Context:
{context}

Conversation History:
{history_text}

Question:
{question}

Answer:
"""

    return prompt