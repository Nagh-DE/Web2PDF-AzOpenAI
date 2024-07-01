from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import Settings
from llama_index.llms.azure_openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def set_llm_config():
    llm = AzureOpenAI(
        model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_API_VERSION"),
    )

    embed_model = AzureOpenAIEmbedding(
        model=os.getenv("AZURE_OPENAI_EMBEDDINGS_MODEL"),
        deployment_name=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_API_VERSION"),
    )

    Settings.llm = llm
    Settings.embed_model = embed_model

    return llm, embed_model
