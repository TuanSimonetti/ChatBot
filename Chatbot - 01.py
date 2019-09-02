from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Protótipo 01')

conversa = ['Oi', 'Olá!', 'Tudo bem?', 'Tudo ótimo.']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Protótipo 01: ', resposta)
    else:
        print('Protótipo 01: Desculpa, ainda não sei responder.')
