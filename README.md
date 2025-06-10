# frigde-ai

A small FastAPI service that generates weekly shopping lists using OpenAI models. The API receives a list of dishes and returns the ingredients you need to buy.

## Prerequisites

- Python 3.11 or newer
- `make`

## Install dependencies

```bash
pip install -r requirements.txt
```

## Set your `OPENAI_API_KEY`

Export your OpenAI API key so that the backend can authenticate requests:

```bash
export OPENAI_API_KEY=<your-key>
```

## Run the server

Start the FastAPI application locally using the provided make target:

```bash
make run
```

The API will be available on <http://localhost:8000>.

## Run the tests

Execute the test suite with `pytest` after installing the dependencies and setting your `OPENAI_API_KEY`:

```bash
pytest
```
