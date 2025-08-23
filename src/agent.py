# src/agent.py
import google.generativeai as genai
from src import config, retriever

# Configure Gemini
genai.configure(api_key=config.GEMINI_API_KEY)

def build_prompt(query: str, retrieved_docs: list) -> str:
    """
    Construct a prompt with retrieved context.
    """
    context = "\n\n".join([doc["content"] for doc in retrieved_docs])
    prompt = f"""
You are an assistant. Use the following context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt

def ask_agent(query: str, k: int = 5) -> str:
    """
    Retrieve context and get an answer from Gemini.
    """
    retrieved_docs = retriever.retrieve(query, k=k)
    prompt = build_prompt(query, retrieved_docs)

    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Interactive Agent (type 'exit' to quit)")
    while True:
        query = input("\nEnter your question: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = ask_agent(query)
        print("\nAgent:", answer)
