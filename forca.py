import random


def jogar():

    imprime_mensagem()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual letra?  ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    print("fim do jogo")
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu.")


def imprime_mensagem():
    print("***************************")
    print("Bem vindo ao jogo da força")
    print("***************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if (__name__ == "__main__"):
    jogar()
