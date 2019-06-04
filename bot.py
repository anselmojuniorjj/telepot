import telepot
from ChatBot import ChatBot

telegram = telepot.Bot('KEY')
bot = ChatBot('Bot')

def recebendoMsg(msg):
    frase2 = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase2)
    # envia resposta para o terminal
    bot.fala(resp)

    # envia resposta para o telegram
        # pegar id do chat telegram
        # chatID = msg['chat']['id']
    # pega id usando telepot
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)


telegram.message_loop(recebendoMsg)

while True:
    pass