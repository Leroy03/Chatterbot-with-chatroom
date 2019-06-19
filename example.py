from chatterbot import ChatBot  # import the chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer  # import chatterbot corpus trainer
import os

# Chatbot for 與機器人聊天
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(bot)  # Trainer for chatterbot

# Import corpus for faster training
corpus_path = './chatterbot_corpus/data/chinese/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)
