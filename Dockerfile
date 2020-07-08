FROM python:3.8.3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install Django

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]