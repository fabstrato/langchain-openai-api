import os
import openai
from dotenv import load_dotenv
from langsmith.wrappers import wrap_openai
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

class HandlerModelo:
    def __init__(self) -> None:
        chave_api_openai = os.environ.get('OPENAI_API_KEY')
        self.converted_api_key = SecretStr(chave_api_openai) if chave_api_openai else None
        self.client = wrap_openai(openai.Client())
        self.model = ChatOpenAI(
            name="gpt-4o-mini", 
            temperature=0, 
            api_key=self.converted_api_key,
        )
        
    def buscar_modelo(self) -> ChatOpenAI:
        return self.model