import gradio as gr
import json
import openai
import os
import logging

from services.constants import params
from services.doc2txt import doc2txt
from services.txt2output import txt2output

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

openai.api_key = os.getenv("OPENAI_API_KEY")

# LangSmith tracking
os.environ["LANGCHAIN_API_KEY"] = params.LANGSMITH_API_KEY
os.environ["LANGCHAIN_ENDPOINT"] = params.LANGCHAIN_ENDPOINT
os.environ["LANGCHAIN_PROJECT"] = params.LANGCHAIN_PROJECT
os.environ["LANGCHAIN_TRACING_V2"] = params.LANGCHAIN_TRACING


def application(input_file):

    try:
        logger.info("Starting...")

        # Loader et extraire texte du document xlsx
        logger.info("Loading xlsx...")
        raw_text = doc2txt(input_file)

        # interroger txt issue avec LLM
        logger.info("Interrogating xlsx...")
        output = txt2output(raw_text)

        # Formater la sortie
        logger.info("Sending Outputs...")

        logger.info("Done !")
        return output
    except Exception as e:
        logger.error("Error : ", str(e))
        return None


with open("themes/dark_theme.json") as file:
    json_string = file.read()
dark_theme_params = json.loads(json_string)

theme = gr.themes.Monochrome(
    font=[gr.themes.GoogleFont("Poppins")],
    font_mono=[gr.themes.GoogleFont("IBM Plex Mono")],
).set(**dark_theme_params)

iface = gr.Interface(
    fn=application,
    inputs=["file"],
    outputs=gr.Markdown(label="xlsx Analyser", show_label=True),
    api_name="xlsx_analyser",
    title="xlsx Analyser",
    description="""Outil augmenté par de l'IA générative \
        conçu pour l'analyse de fichiers au format XLSX (Excel)""",
    allow_flagging="never",
    theme=theme
).launch()

# Lancer l'interface
iface.launch(server_name=params.SERVER_NAME,
             server_port=params.SERVER_PORT)
