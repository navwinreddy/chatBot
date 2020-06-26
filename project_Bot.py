from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('My Bot')

#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train('chatterbot.corpus.english')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "sure, I would like to order some food.",
    "please confirm your order."
])

print('Bot: ', 'Hi there!')
while True:
    request = input('You:  ')
    response = chatbot.get_response(request)
    print('Bot: ', response)