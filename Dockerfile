FROM python:3

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install aioboto3
RUN pip install python-dotenv

CMD [ "python", "server.py" ]
