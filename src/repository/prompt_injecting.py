from config import PROMPT
from src.domain.dish_request import DishRequest


def prompt_injecting(dish_request: DishRequest):
    return PROMPT.replace("dish_request", ', '.join(dish_request.dishes))