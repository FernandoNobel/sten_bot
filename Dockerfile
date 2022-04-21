FROM python:3.8

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY . . 

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
