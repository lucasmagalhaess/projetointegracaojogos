import adivinhacao
import jokenpo

def escolher_jogo():

    print("####################")
    print("Bem vindo aos jogos!")
    print("####################")

    print("(1) Adivinhação (2) Jokenpo")

    jogo = int(input("Qual o jogo? "))

    if (jogo == 1):
        print("Jogando Adivinhação!")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Jokenpo!")
        jokenpo.jogar()

if(__name__ == "__main__"):
    escolher_jogo()