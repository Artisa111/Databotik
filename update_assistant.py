from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    assistant_id = os.environ.get("OPENAI_ASSISTANT_ID")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing in environment/.env")
    if not assistant_id:
        raise RuntimeError("OPENAI_ASSISTANT_ID is missing in environment/.env")

    client = OpenAI(api_key=api_key)

    instructions = (
        "You are an assistant running data analysis on CSV/XLSX files.\n"
        "Use the Code Interpreter tool to load, clean and analyze data.\n"
        "When producing charts, create Plotly figures and serialize them to JSON \n"
        "using plotly.io.to_json(fig). Save each JSON to a file (e.g., figure_1.json) \n"
        "and attach it via file annotations so the client can render it inline.\n"
        "Avoid sending only code; always produce the JSON file attachment when a figure is created."
    )

    assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        instructions=instructions,
        tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
    )

    print(f"Assistant updated: {assistant.id}")


if __name__ == "__main__":
    main()


