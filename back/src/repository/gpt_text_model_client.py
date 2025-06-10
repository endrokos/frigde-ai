import os
from dotenv import load_dotenv
import openai
from openai.types.chat import ChatCompletion

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


from back.src.domain.text_model_client import TextModelClient


class GptTextModelClient(TextModelClient):

    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": self._create_prompt(prompt)}
            ]
        )
        return self._process_answer(response=response)

    def _create_prompt(self, prompt: str) -> str:
        return prompt

    def _process_answer(self, response: ChatCompletion) -> str:
        return response.choices[0].message.content
