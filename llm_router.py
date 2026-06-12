import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def choose_tool(query):

    prompt = f"""
You are a tool routing system.

Available tools:

SQL:
- company records
- lawsuits
- fines
- legal cases
- structured database information
- companies like Amazon, Google, Meta, Apple, Microsoft

VECTOR:
- policies
- regulations
- GDPR
- legal documents
- document search
- semantic search

WEB:
- latest news
- current events
- recent updates
- information happening today

GENERAL:
- programming questions
- algorithms
- computer science
- explanations
- definitions
- general knowledge
- questions that do not require SQL, VECTOR, or WEB

Question:
{query}

Rules:

- Questions about lawsuits, fines, settlements, legal cases, or company violations -> SQL
- Questions about regulations, policies, GDPR, compliance, legal documents, or document retrieval -> VECTOR
- Questions about latest news, current events, recent updates, CEOs, founders, company information, live information, or facts that may change over time -> WEB
- Programming questions, algorithms, coding help, explanations, definitions, computer science topics, and general knowledge -> GENERAL
Examples:

Amazon privacy lawsuit -> SQL

Google fined for privacy violations -> SQL

GDPR regulations -> VECTOR

Latest AI news -> WEB

Who is Google's CEO? -> WEB

Who founded Microsoft? -> WEB

What is merge sort? -> GENERAL

Explain recursion -> GENERAL

What is Python? -> GENERAL

Respond with exactly one word:

SQL
VECTOR
WEB
GENERAL
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    while True:

        query = input("\nQuestion: ")

        if query.lower() == "exit":
            break

        tool = choose_tool(query)

        print(f"\nSelected Tool: {tool}")