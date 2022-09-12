numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("digite o seu numero:")
    print("voce digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("você acertou !")
        break
    else:
        if (maior):
            print("Você errou! O seu chhute foi maior do que o numero secreto.")
        elif (menor):
            print("Você errou! O seu chhute foi menor do que o numero secreto.")

print("fim do jogo")
