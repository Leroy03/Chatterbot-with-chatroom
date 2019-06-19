from chatterbot import ChatBot  # import the chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer  # import chatterbot corpus trainer
import os

# Chatbot for 一般人連線聊天
bot2 = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database2.db',
    read_only=True,
)

trainer = ChatterBotCorpusTrainer(bot2)  # Trainer for chatterbot

# Import corpus for faster training
corpus_path = './chatterbot_corpus/data/chinese/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)