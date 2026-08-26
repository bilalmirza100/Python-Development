FROM python:3.11-slim
WORKDIR /app

RUN pip install fastapi uvicorn sqlalchemy asyncpg pydantic

COPY ./marketplace /app/marketplace

EXPOSE 8000
CMD ["uvicorn", "marketplace.main:app", "--host", "0.0.0.0", "--port", "8000"]