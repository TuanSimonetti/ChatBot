from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Protótipo')

conversa = ['Oi', 'Ola', 'Tudo bem?', 'Tudo otimo']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = str(input('Usuário: '))
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Portotipo: ', resposta)
    else:
        print('Prototipo: Desculpa, eu não sei.')
