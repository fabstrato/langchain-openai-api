from langsmith import traceable
from langchain_core.prompts import ChatPromptTemplate

class HandlerChatbot:
    def __init__(self, handler_modelo) -> None:
        self.handler_modelo = handler_modelo

    @traceable
    def gerar_retorno_chatbot(self, input_requisicao: str, prompt: str) -> str:

        model = self.handler_modelo.buscar_modelo()
        
        prompt_com_modelo = ChatPromptTemplate.from_messages(
            [
                ("system", prompt),
                ("human", input_requisicao)
            ]
        ) | model
        
        output = prompt_com_modelo.invoke({
            "input_requisicao": input_requisicao,
            "prompt": prompt,
        })

        return output.content