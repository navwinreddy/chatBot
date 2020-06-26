FROM python:3
RUN pip install -U chatterbot
RUN pip install pip install -U chatterbot_corpus
ADD project_Bot.py /
CMD [ "python", "./project_Bot.py" ]

