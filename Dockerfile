FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install pyproject.toml
