from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Protótipo 03')

conversa = ['Oi', 'Ola',
            'Tudo bem?', 'Tudo otimo',
            'Você sabe inglês?', 'Yes, I know.',
            'What is your name?', 'My name is {}'.format(str(input("I don't know. Waht's my name?"))),
            'What do you do?', "I'm your virtual assistent. But, I'm in the fase of learn. And you: what do you do?",
            "I'm a programmer. Do you like this?", 'I think that is very interestanting',
            'What do you like?', 'I like conversation. Because,I can leanin with chat.',
            'Do you like sports?', 'I like, but, I can not pratictice. Because, I do not have body. kkkkkkkkkk']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = str(input('Usuário: '))
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Portotipo: ', resposta)
    else:
        print('Prototipo: Desculpa, eu não sei.')
