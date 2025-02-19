FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install -r req.txt

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "80"]
