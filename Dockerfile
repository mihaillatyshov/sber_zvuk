FROM python:3

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install aioboto3
RUN pip install python-dotenv
RUN pip install SpeechRecognition
RUN pip install moviepy
#RUN pip install pydub
#RUN pip install baidu-api
#RUN pip install vosk

CMD [ "python", "server.py" ]
