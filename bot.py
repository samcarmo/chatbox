# importando a classe ChatBot do pacote chatterbot
from chatterbot import ChatBot


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# criando o bot
chatbot = ChatBot("Talk2ai", tagger_language=ENGSM)
# método para start da app
if __name__ == "__main__":
    name = input("Qual o seu nome?")
    # laço para repetir o processo até que seja digitado '/stop'
    while True:
        msg = input(f"{name} disse:")
        if msg == "/stop":
            print(f"Por favor {name}, não me deixe sozinha!!!")
            print(f"{name}, porque você matou a T2AI?")
            break
        #          mandando o texto digitado para o bot treinado
        #          o bot devolve uma resposta
        response = chatbot.get_response(msg)
        print(f"T2AI disse: {response}")
