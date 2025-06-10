from typing import Dict

from back.src.domain.dish_request import DishRequest
from back.src.repository.gpt_text_model_client import GptTextModelClient
from back.src.repository.prompt_injecting import prompt_injecting


def generate_shopping_list_use_case(dish_request: DishRequest, text_model_client: GptTextModelClient) -> Dict:
    prompt = prompt_injecting(dish_request)
    try:
        response = text_model_client.generate(prompt)
        return {"shopping_list": response}
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {"shopping_list": "Algo salió mal :("}
