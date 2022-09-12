
import random


def jogar():

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade ?")
    print("(1)facil (2)medio (3)dificil")

    nivel = int(input("Defina o nivel de dificuldade:"))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("digite o seu numero:")
        print("voce digitou", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        if (acertou):
            print("você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o numero secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")


if (__name__ == "__main__"):
    jogar()
