from tools.answer_formatter import format_answer
from llm_router import choose_tool

from tools.vector_tool import vector_search
from tools.sql_tool import sql_search
from tools.web_tool import web_search
from tools.general_tool import general_answer


def run_agent(query, history=None):

    if history is None:
        history = []

    # Build conversation context
    conversation = ""

    for msg in history[-10:]:
        sender = msg.get("sender", "")
        text = msg.get("text", "")
        conversation += f"{sender}: {text}\n"

    conversation += f"user: {query}"

    tool = choose_tool(conversation)

    print(f"\nSelected Tool: {tool}")

    if tool == "SQL":
        raw_result = sql_search(conversation)
        return format_answer(conversation, raw_result)

    elif tool == "VECTOR":
        raw_result = vector_search(conversation)
        return format_answer(conversation, raw_result)

    elif tool == "WEB":
        raw_result = web_search(conversation)
        return format_answer(conversation, raw_result)

    elif tool == "GENERAL":
        return general_answer(conversation)

    else:
        return "Could not determine the correct tool."


if __name__ == "__main__":

    while True:

        query = input("\nAsk a question: ")

        if query.lower() == "exit":
            break

        result = run_agent(query)

        print("\nRESULT:")
        print(result)