from fastapi import FastAPI

from config import MODEL_NAME
from back.src.application.use_cases import generate_shopping_list_use_case
from back.src.domain.dish_request import DishRequest
from back.src.repository.gpt_text_model_client import GptTextModelClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


origins = ["http://localhost:3000", "https://endrokosai.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-shopping-list")
def generate_shopping_list(dishes: DishRequest):
    gpt_text_model_client = GptTextModelClient(model_name=MODEL_NAME)
    return generate_shopping_list_use_case(dish_request=dishes, text_model_client=gpt_text_model_client)