import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def web_search(query: str):
    try:
        client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

        response = client.search(
            query=query,
            search_depth="basic",
            max_results=3
        )

        return response

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    result = web_search(
        "latest AI news"
    )

    print(result)