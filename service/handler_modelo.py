import os
import openai
from dotenv import load_dotenv
from langsmith.wrappers import wrap_openai
from langchain_openai import ChatOpenAI

load_dotenv()

class HandlerModelo:
    def __init__(self) -> None:
        self.client = wrap_openai(openai.Client())
        self.model = ChatOpenAI(
            name="gpt-4o-mini", 
            temperature=0, 
        )
        
    def buscar_modelo(self) -> ChatOpenAI:
        return self.model