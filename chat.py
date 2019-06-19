from chatterbot import ChatBot
import logging
"""反饋式的聊天機器人，會根據你的反饋進行學習"""
# 把下面這行前的註釋去掉，可以把一些資訊寫入日誌中
# logging.basicConfig(level=logging.INFO)
# 建立一個聊天機器人
bot = ChatBot(
   'Feedback Learning Bot',
   storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
   logic_adapters=[
       'chatterbot.logic.BestMatch'
   ],
   input_adapter='chatterbot.input.TerminalAdapter',
 output_adapter='chatterbot.output.TerminalAdapter')
DEFAULT_SESSION_ID = bot.default_session.id

print('Type something to begin...')
# 每次使用者有輸入內容，這個迴圈就會開始執行
while True:
   try:
       input_statement = bot.input.process_input_statement()
       statement, response = bot.generate_response(input_statement, DEFAULT_SESSION_ID)
       print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))
       bot.output.process_response(response)
       # 更新chatbot的歷史聊天資料
       bot.conversation_sessions.update(
           bot.default_session.id_string,
           (statement, response, )
       )
   # 直到按ctrl-c 或者 ctrl-d 才會退出
   except (KeyboardInterrupt, EOFError, SystemExit):
       break

from chatterbot import ChatBot
import logging
'''這是一個使用Ubuntu語料構建聊天機器人的例子'''
# 允許打日誌logging.basicConfig(level=logging.INFO)
chatbot = ChatBot(
   'Example Bot',   trainer='chatterbot.trainers.UbuntuCorpusTrainer')
# 使用Ubuntu資料集開始訓練
chatbot.train()
# 我們來看看訓練後的機器人的應答
response = chatbot.get_response('How are you doing today?')
print(response)