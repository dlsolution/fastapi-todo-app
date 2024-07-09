FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.8.3
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 8000