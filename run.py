from chatterbot import ChatBot
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


def main():
    bot = Bot()
    bot.run()


# def mdata(txt):
#     chatbot = ChatBot(
#     'flash',
#     trainer='chatterbot.trainers.ListTrainer'
#     )
#     response = chatbot.get_response(txt.body['text'])
#     return response
    
@respond_to('', re.IGNORECASE)
def hi(message):
    print(message.body['text'])
    res = getdata(message.body['text'])
    message.send(res)
    # react with thumb up emoji
    message.react('+1')



def getdata(txt):
    chatbot = ChatBot(
    'flash',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )
    response = chatbot.get_response(txt)
    print(response)
    return str(response)

if __name__ == "__main__":
    main()