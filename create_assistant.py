from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


instructions = """You are an assistant running data analysis on CSV files.

You will use code interpreter to run the analysis.

However, instead of rendering the charts as images, you will generate a plotly figure and turn it into json.
You will create a file for each json that I can download through annotations.
"""

tools = [
    {"type": "code_interpreter"},
    {"type": "file_search"}
]

sample_file_path = os.environ.get("SAMPLE_CSV_PATH")
file = None
if sample_file_path and os.path.exists(sample_file_path):
    file = openai_client.files.create(
      file=open(sample_file_path, "rb"),
      purpose='assistants'
    )


assistant = openai_client.beta.assistants.create(
    model="gpt-4o",
    name="Data Analysis Assistant",
    instructions=instructions,
    temperature=0.1,
    tools=tools,
    tool_resources=(
        {"code_interpreter": {"file_ids": [file.id]}} if file else None
    )
)

print(f"Assistant created with id: {assistant.id}")