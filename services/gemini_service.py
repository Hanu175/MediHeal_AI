from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage

from config.settings import llm


class GeminiService:

    @staticmethod
    def generate(system_prompt: str, prompt: str):

        messages = [

            SystemMessage(content=system_prompt),

            HumanMessage(content=prompt)

        ]

        response = llm.invoke(messages)

        return response.content