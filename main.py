# at python 3.6
# pip install chatterbot
# pip install spacy
# importando a classe ChatBot do pacote chatterbot
from chatterbot import ChatBot

# importando a classe ListTraine do pacote chatterbot.trainers
from chatterbot.trainers import ListTrainer

# isso aqui só precisa para corrigir o bug ------------------------
from spacy.cli import download

download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


#     -------------------------------------------------------------

# var_chatbot recebe a criação de um novo bot, obj do tipo ChatBot
#                nome do bot , class de config idioma e formato
chatbot = ChatBot("Talk2ai", tagger_language=ENGSM)

conversation = [
    "Oi", "Olá, tudo bem?",
    "sim", "legal",
    "não", ":(",
    "nada", "tédio...", "nd", "tédio",
    "mau", ":(", "triste", ":(", "horrível", ":(", "terrível", ":(",
    "bem", "legal :D", "também", "legal :D", "claro", "legal :D", "lógico", "legal :D",
    "SENAI", "não conheço",
    "paz", "#paz :D",
    "Tudo bem", "Que bom, o que faz aí?",
    "Nada e você?", "Ah, estou aqui no tédio...",
    "Você estuda?", "Claro, enquanto conversamos estou aprendendo com você",
    "O que gosta de fazer em dias de folga?", "Dormir, kkkkkkkkkk",
    "Gosta de futebol?", "Exercício físico é ruim, prefiro ficar no computador",
    "Conhece a Alexa?", "Sim, mas não pessoalmente",
    "Conhece a Google Home?", "Sim, nós teclamos ontem",
    "Conhece o Palmeiras?", "Claro, melhor time do Brasil",
    "qual time vc torce?", "Flamengo :D",
    "qual time vc torce?", "Vasco :D",
    "qual time vc torce?", "São Paulo :D",
    "qual time vc torce?", "Grêmio :D"
]
# criar um objeto de treinamento para o bot
trainer = ListTrainer(chatbot)
# executar o treinamento do bot
trainer.train(conversation)