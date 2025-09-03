import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)