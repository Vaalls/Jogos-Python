import random
def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentaivas = 0
    pontos = 1000

    print("Qual nivel de dificuldade você deseja? ")
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentaivas = 20
    elif(nivel == 2):
        total_de_tentaivas = 10
    else:
        total_de_tentaivas = 5

    for rodada in range(1, total_de_tentaivas + 1):
        print("Tentativa: {} de {}".format(rodada,  total_de_tentaivas))

        chute_str = input("Digite seu número!  ")
        chute = int(chute_str)
        print("você chutou o número ",  chute_str)

        if(chute < 0 or chute > 100):
            print("Você deve chutar um número entre 1 e 100")
            continue


        acertou = chute == numero_secreto
        menor   = chute < numero_secreto
        maior   = chute > numero_secreto

        if(acertou):
            print("Você acertou!! E fez {} pontos ".format(pontos) )
            print("Fim de jogo!")
            break
        else:
            if(menor):
                print("Você errou!! Seu chute foi menor que o numero secreto")
            elif(maior):
                print("Você errou!! Seu chute foi maior que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos_perdidos - pontos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
