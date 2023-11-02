import os
from dotenv import load_dotenv

model = "GPT3.5"
# model = "GPT4"


class params():

    load_dotenv()

    if model == "GPT3.5":
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_GPT35")

        OPENAI_API_TYPE = "azure"
        OPENAI_API_BASE = "https://redflags.openai.azure.com/"
        OPENAI_API_VERSION = "2023-03-15-preview"

        OPENAI_GPT_DEPLOYMENT_NAME = "rf-gpt35"
        OPENAI_GPT_MODEL_NAME = "gpt-35-turbo"

    elif model == "GPT4":
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_GPT4")

        OPENAI_API_TYPE = "azure"
        OPENAI_API_BASE = "https://openai-suisse.openai.azure.com/"
        OPENAI_API_VERSION = "2023-07-01-preview"

        OPENAI_GPT_DEPLOYMENT_NAME = "suisse"
        OPENAI_GPT_MODEL_NAME = "gpt-4"

    OPENAI_API_TYPE_EMBEDDING = "azure"
    OPENAI_API_BASE_EMBEDDING = "https://redflags.openai.azure.com/"
    OPENAI_API_VERSION_EMBEDDING = "2023-03-15-preview"

    OPENAI_DEPLOYMENT_NAME_EMBEDDING = "rf-ada2"
    OPENAI_MODEL_NAME_EMBEDDING = "text-embedding-ada-002"

    MAX_PAGES = 400
    MODEL_CONTEXT_WINDOW = 8192
    CHUNK_SIZE = MODEL_CONTEXT_WINDOW * 3

    XLSX_HUMAN_TEMPLATE_PATH = "data/inputs/red_flags_template_human.xlsx"
    XLSX_MACHINE_TEMPLATE_PATH = "data/inputs/red_flags_template_AI.xlsx"
    XLSX_OUTPUT_PATH = "data/outputs/red_flags_output.xlsx"
    PDF_PATH = "data/temp.pdf"

    # LangSmith
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
    LANGCHAIN_PROJECT = "RedFlags"
    LANGCHAIN_TRACING = "true"

    # server
    if 'WEBSITE_SITE_NAME' in os.environ:
        # running in the cloud
        SERVER_PORT = 8000
        SERVER_NAME = "0.0.0.0"
    else:
        # running locally
        SERVER_PORT = None
        SERVER_NAME = None
