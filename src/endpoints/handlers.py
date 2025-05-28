from fastapi import FastAPI

from config import MODEL_NAME
from src.application.use_cases import generate_shopping_list_use_case
from src.domain.dish_request import DishRequest
from src.repository.gpt_text_model_client import GptTextModelClient

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.post("/generate-shopping-list")
def generate_shopping_list(dishes: DishRequest):
    gpt_text_model_client = GptTextModelClient(model_name=MODEL_NAME)
    return generate_shopping_list_use_case(dish_request=dishes, text_model_client=gpt_text_model_client)