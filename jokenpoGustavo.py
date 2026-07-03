print("BEM VINDO AO MEGABLASTER JOKENPO 2000000")
print("------------------------------------------")
import random
pontuacao01 = 0
pontuacao02 = 0
 
def ganhar():
    if pontuacao01 == 5:
        print("Parabens, Você ganhou o jogo! :) ")
        denovo = input("Você quer jogar denovo? | 1 - Sim | 2 - Não: ").strip()
        if denovo.strip() == "":
            print("Campo vazio")
            continue
        if denovo == "1":
            pontuacao02 = 0
            pontuacao01 = 0
        if denovo == "1":
            print("Você voltou para o jogo")
        elif denovo == "2":
            break
        else:
            print("Selecione uma opção válida")
            continue
    
    elif pontuacao02 == 5:
        print("Infelizmente Você perdeu :( ")
        revanche = input("Você quer jogar denovo? | 1 - Sim | 2 - Não: ").strip()
        if revanche.strip() == "":
            print("Campo vazio")
            continue
 
        if revanche == "1":
            pontuacao01 = 0
            pontuacao02 = 0
 
        elif revanche == "1":
            print("Você voltou")
 
        elif revanche == "2":
            print("Você saiu do jogo :( ")
            break
        else:
            print("Selecione uma opção válida")
            continue

def jogo():
    opcao = input("Digite: 1-Papel | 2-Pedra | 3-Tesoura | 0-Sair: ").strip()
    if opcao.strip() == "":
        print("Campo vazio | Selecione um caractere válido")
        continue
 
    elif opcao == "0":
        print("Sério? ok né | Você encerrou o jogo")
        break
 
    elif opcao == "1" and x == "2":
        print("Você jogou papel, e o computador jogou pedra | Você ganhou!")
        pontuacao01 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == "2" and x == "3":
        print("Você jogou pedra, e o computador jogou tesoura | Você ganhou!")
        pontuacao01 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == "3" and x == "1":
        print("Você jogou tesoura, e o computador jogou papel | Você ganhou!")
        pontuacao01 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == "3" and x == "2":
        print("Você jogou tesoura, e o computador jogou pedra | Maquina ganhou!")
        pontuacao02 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == "2" and x == "1":
        print("Você jogou pedra, e o computador jogou papel | Maquina ganhou!")
        pontuacao02 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == "1" and x == "3":
        print("Você jogou papel, e o computador jogou tesoura | Maquina ganhou!")
        pontuacao02 += 1
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
 
    elif opcao == x:
        print("EMPATE!!!")
        print(f"Você está com {pontuacao01} e a Maquina com {pontuacao02}")
        continue
 
    else:
        print("Selecione um caratere válido")
        continue
 


while True:
 
    ganhar()
 
    x = str(random.randint(1,3))
 
    jogo()
