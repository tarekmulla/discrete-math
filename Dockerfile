FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./webapp ./app
WORKDIR /app

EXPOSE 80

CMD ["python", "run.py"]
