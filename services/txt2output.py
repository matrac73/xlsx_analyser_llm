import logging

from services.templates import Template
from services.constants import params
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.chains.summarize import load_summarize_chain

logger = logging.getLogger(__name__)


def txt2output(raw_text):
    try:
        llm = AzureChatOpenAI(
            deployment_name=params.OPENAI_GPT_DEPLOYMENT_NAME,
            model_name=params.OPENAI_GPT_MODEL_NAME,
            openai_api_base=params.OPENAI_API_BASE,
            openai_api_type=params.OPENAI_API_TYPE,
            openai_api_version=params.OPENAI_API_VERSION,
            temperature=0,
            request_timeout=120,
            max_retries=10,
            openai_api_key=params.OPENAI_API_KEY,
        )

        map_template = Template().map_key_insights
        combine_template = Template().combine_key_insights
        collapse_template = Template().collapse_key_insights

        map_prompt = PromptTemplate(
            template=map_template,
            input_variables=["text"])
        collapse_prompt = PromptTemplate(
            template=collapse_template,
            input_variables=["text"])
        combine_prompt = PromptTemplate(
            template=combine_template,
            input_variables=["text"])

        chain = load_summarize_chain(
            llm=llm,
            chain_type="map_reduce",
            return_intermediate_steps=True,
            map_prompt=map_prompt,
            combine_prompt=combine_prompt,
            collapse_prompt=collapse_prompt,
            token_max=params.MODEL_CONTEXT_WINDOW,
        )

        # steps = chain(
        #     {"input_documents": raw_text},
        #     return_only_outputs=True)

        # output = steps["output_text"]
        output = raw_text

        return output

    except Exception as e:
        logger.error("Error : ", str(e))
        return None
