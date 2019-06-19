from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database-test.db'
)

trainer = ChatterBotCorpusTrainer(bot)

#corpus_path = '/home/toby/下載/chatterbot-corpus-master/chatterbot_corpus/data/chinese/'

trainer.train('chatterbot.corpus.chinese')

"""
for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

"""
"""
while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)
"""