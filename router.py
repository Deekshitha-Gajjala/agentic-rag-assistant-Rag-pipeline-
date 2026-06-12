from tools.vector_tool import vector_search
from tools.sql_tool import sql_search
from tools.web_tool import web_search


def route_query(query):
    query_lower = query.lower()

    # Web Tool
    if any(word in query_lower for word in [
        "latest",
        "today",
        "news",
        "recent",
        "current"
    ]):
        print("\nUsing Web Tool...\n")
        return web_search(query)

    # SQL Tool
    elif any(word in query_lower for word in [
        "amazon",
        "google",
        "meta",
        "apple",
        "microsoft",
        "twitter",
        "tiktok",
        "case",
        "lawsuit"
    ]):
        print("\nUsing SQL Tool...\n")
        return sql_search(query)

    # Vector Tool
    else:
        print("\nUsing Vector Tool...\n")
        return vector_search(query)


if __name__ == "__main__":

    while True:

        user_query = input("\nAsk a question (type exit to quit): ")

        if user_query.lower() == "exit":
            break

        result = route_query(user_query)

        print("\nRESULT:")
        print(result)