import random

def jogar():

    print("|-----------------------------------|")
    print("| Bem vindo ao jogo de Adivinhação! |")
    print("|-----------------------------------|")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil | (4) Muito Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    elif(nivel == 3):
        total_de_tentativas = 3
    else:
        total_de_tentativas = 1            


    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa: {rodada}/{total_de_tentativas}')

        numero_usuario_str = input("Digite o seu número entre 1 e 100: ")
        numero_usuario = int(numero_usuario_str)

        if(numero_usuario < 1 or numero_usuario > 100):
            print("O número precisa ser entre 1 e 100")
            continue

        acertou = numero_secreto == numero_usuario
        secreto_maior = numero_secreto > numero_usuario
        secreto_menor = numero_secreto < numero_usuario

        print("--------------------------------------------------------------")
        if (acertou):
            print(f'Você acertou o número secreto {numero_secreto} e fez {pontos} pontos')
            break
        else:
            if(secreto_maior):
                print("Você errou, o número secreto é maior do que o seu palpite!")
            elif (secreto_menor):
                print("Você errou, o número secreto é menor do que o seu palpite!")
            print("--------------------------------------------------------------")    
            pontos_perdidos = abs(numero_secreto - numero_usuario)
            pontos = pontos - pontos_perdidos        

    print("--------------------------------------------------")
    print(f'      O número secreto era: {numero_secreto}     ')
    print("--------------------------------------------------")
    print("------------------ Fim de Jogo! ------------------")    

if(__name__ == "__main__"):
    jogar()       