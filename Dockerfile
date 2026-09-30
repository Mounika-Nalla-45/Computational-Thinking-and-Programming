FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install pytest mypy

CMD ["python", "app.py"]