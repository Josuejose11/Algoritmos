import random 
from datetime import date
import math


# 
#  # num1=10
# # num2=5
# # b=num1
# # h=num2
# # print (f"A área do retangulo é de: {b*h}m²")

# # nome = input("qual seu nome: ")
# # idade= int(input("quantos anos voce tem:"))
# # cidade = input("onde voce mora:")
# # print (f"Olá {nome}!\nVocê tem {idade} anos e mora em {cidade} .")

# # num1 = float(input("escolha um numero:"))
# # num2 = float(input("escolha outro numero:"))
# # print (f"{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\n{num1} * {num2} = {num1*num2}\n{num1}/{num2} = {num1/num2}")

# # print ("Você está em um conversor de temperatura.")
# # num1 = float(input("Escolha uma temperatura em graus celsius: "))
# # print (f"F°={num1*1.8+32}")

# # print ("Você está em uma calculadora de IMC.")
# # num2 = float(input("Qual o seu peso: "))
# # num3 = float(input("Qual a sua altura: "))
# # print (f"IMC={num2/num3**2}")

# # print ("Você está em um conversor de moedas.")
# # num4 = float(input("Qual seu valor em reais: "))
# # print (f"Dollar é ={num4/5.20}")

# # idade=16
# # if idade >= 18:
# #    print ("maior")
# # else:
# #    print ("menor")

# # if idade >= 16:
# #    print ("pode votar")


# # num = float(input("Me de um numero: "))
# # if num >=0 and num <= 10:
# #    print ("seu numero esta entre 0 e 10")
# # else:
# #    print ("seu numero nao esta entre 0 e 10")


# # nota1 = float(input("Me diga a nota da sua prova: "))
# # nota2 = float(input("Me diga a nota do seu trabalho: "))
# # nota3 = float(input("Me diga a nota da sua avaliacao: "))

# # media = (nota1+nota2+nota3)/3

# # if media >= 9 and media <= 10:
# #   print ("Você tirou o conceito A")
# # elif media >= 7 and media <9:
# #    print ("Você tirou o conceito B")
# # elif media >= 5 and media <9:
# #    print ("Você tirou o conceito c")
# # elif media <= 5 and media <9:
# # print ("Você tirou o conceito D")


# # nota1 = float(input("Me diga a nota da sua prova: "))
# # nota2 = float(input("Me diga a nota do seu trabalho: "))
# # nota3 = float(input("Me diga a nota da sua avaliacao: "))

# # media = (nota1+nota2+nota3)/3

# # if media >= 9 and media <= 10:
# #   conceito = "A"
# # elif media >= 7 and media <9:
# #   conceito = "B"
# # elif media >= 5 and media <9:
# #   conceito = "C"
# # elif media <= 5 and media <9:
# #    conceito = "D"

# # print (f"Você tirou o conceito {conceito}") 

# # usuario = input ("qual seu login? ")
# # senha = input ("qual sua senha? ")

# # if usuario == "bruno":
# #    if senha == "1234":
# #        print ("Você entrou como administrador")
# #    else:
# #        print ("senha incorreta")   
# # else:
# #     if senha == "4321":
# #        print ("Você entrou como usuario comum")
# #    else:
# #        print ("senha incorreta")   

# # numero = int(input("Escolha um numero qualquer: "))
# # print ("é par" if numero %2 == 0 else "é impar")

# # idade = int(input("Qual a sua idade: "))
# # maiorDeIdade = "Maior de idade" if idade>=18 else "Menor de idade"
# # print (maiorDeIdade)

# # nota = float(input("qual a sua nota: "))
# # nota1 = "aprovado" if nota>=7 else "Reprovado"
# # print (nota1)

# # senha = input("qual a sua senha: ")
# # senha1 = "Sua senha esta correta" if senha == "1234" else "Sua senha esta incorreta"
# # print (senha1)

# # from datetime import datetime
# # horario= datetime.now().hour
# # print ("bom dia" if horario <=12 else "boa tarde")

# # numero = int(input("escolha um numero: "))
# # print (f"O numero {numero} é par" if numero )

# # campo_int = None

# # if campo_int is not None:
# #     print("O campo foi preenchido.")
# # else:
# #     print("O campo está vazio (None).")

# # numero = int(input("escolha um numero: "))
# # if numero>0:
# #     print ("Seu numero é positivo")
# # elif numero==0:
# #     print ("O seu numero é 0")
# # elif numero<0:
# #     print ("o seu numero é negativo")

# # idade = int(input("Qual a sua idade? "))
# # if idade>0 and idade<4:
# #     print ("Você é um bebe")
# # elif idade>=4 and idade<=12:
# #     print ("Você é uma criança")
# # elif idade>12 and idade<18:
# #     print ("Você é um adolescente")
# # elif idade>=18 and idade<60:
# #     print ("Você é um adulto")

# # nota = float(input("Qual a sua nota: "))
# # if nota>6 and nota<=10:
# #     print ("Você esta aprovado")
# # elif nota>3 and nota<7:
# #     print ("Você esta de recuperacao")
# # elif nota<4 and nota>0:
# #     print ("Você esta reprovado")

# # num = int(input("Escolha um numero: "))
# # num_novo = num.replace (" ", "")
# # print("é par" if num % 2 == 0 else "é impar")

# # senha = (input("qual sua senha: "))
# # senha_nova = senha.replace (" ", "")
# # if senha_nova == "":
# #     print ("sua senha nao esta validada")
# # else:
# #     print ("sua senha esta validada")



# # import random

# # num2 = random.randint(1,10)
# # num1 = 0
# # while num1 != num2:
# #     num1 = int(input("Um numero de 1 a 10: "))
# #     if num1 == num2:
# #         print ("voce acertou o numero")



# # valor = float(input("Valor da compra: "))

# # if valor <= 100:
# #     valorSD = valor
# #     print(f"Valor final: {valorSD}")
# # elif valor > 100 and valor <300:
# #     valorCD1 = valor *90/100
# #     print(f"Valor final: {valorCD1}")
# # elif valor >300:
# #     valorCD2 = valor*80/100
# #     print(f"Valor final: {valorCD2}")


# # import random

# # num2 = random.randint(1,100)
# # num1 = int(input("escolha um numero de 1 a 100: "))

# # if num1 == num2:
# #     print("Você acertou o numero!")
# # else:
# #     while num1 != num2:
# #         if num2>num1:
# #                 num1 = int(input("Você errou, o número escolhido é maior, escolha outro numero de 1 a 100: "))
# #                 if num1 == num2:
# #                     print ("voce acertou o numero")
# #         else:
# #             num1 = int(input("Você errou, o número escolhido é menor, escolha outro numero de 1 a 100: "))
# #             if num1 == num2:
# #                 print ("voce acertou o numero")

# # senha = (input("qual sua senha: "))
# # # senha_nova = senha.replace (" ", "")
# # # if senha_nova == "":
# # #     print ("sua senha nao esta validada")
# # # else:
# # #     print ("sua senha esta validada")
# # if not senha.strip():
# #     print ("a senha nao pode estar vazia")

# # elif len(senha) < 8:
# #     print("a senha deve conter menos de 8 caracteres")
# # else:
# #     print ("senha invalida")


# nome = input("qual seu nome: ")

# def saudacao(nome):
#     print(f"ola {nome}, seja bem vindo(a)")

# saudacao(nome)


# condicao=True

# while condicao:
#     print ("oi")   #Ctrl C - para parar o laço infinito (no terminal)
#     condicao += 1

# num1 = 0

# while num1<=10:
#     print (f"seu Numero é {num1}")
#     num1 += 1

# print ("FIM!")

# num2 = 10

# while num2>0:
#     print (f"seu Numero é {num2}")
#     num2 -= 1

# print ("FIM!")

# num3 = 0

# while num3<=100:
#     print (f"seu Numero é {num3}")
#     num3 += 10

# print ("FIM!")


       
# num1 = int(input("escolha um numero de 0 a 10: "))
# contador= 1

# while num1 != 5:
#     if contador <=15:
#         num1=int(input("voce errou, escolha outro numero: "))
#         contador += 1
#     else:
#         print ("Você atingiu o numero maximo de tentativas")
#         break

# else:
#     print(f"\n Você acertou o numero com {contador} tentativas")





# #jogo legal

# import random

# num2 = random.randint(1,100)
# num1 = int(input("escolha um numero de 1 a 100: "))

# while num1 != num2:
#     if num2>num1:
#         num1 = int(input("Você errou, o número escolhido é maior, escolha outro numero de 1 a 100: "))
#     else:
#         num1 = int(input("Você errou, o número escolhido é menor, escolha outro numero de 1 a 100: "))

# if num1 == num2:
#     print ("voce acertou o numero")

# for i in range (1,6):
#     print (i)

# for i in range (0,10, 2):
#     print (i)

# numtab= int(input("Escolha uma tabuada para visualizar: "))

# for i in range (1,11):
#     print (f"{numtab} x {i} = {numtab*i}")

# numfat= int(input("Escolha uma numero para visualizar o seu fatorial: "))
# total = 1

# for i in range (2, numfat+1):
#     total*=i

# print (f"{numfat}! = {total}")

# # ".strip" retira espaço
# # strip vazia = false

# while True:
#     print ("================== \nBem vindo a calculdora!! \nEscolha uma opção. \n==================")
#     print ("0 - sair")
#     print ("1 - Adição")
#     print ("2 - Subtração")
#     print ("3 - Multiplicação")
#     print ("4 - Divisão")

#     escolha = input()
#     if escolha == "0":
#         print ("Você saiu")
#         break
    
#     num1 = input ("Qual seu 1° numero: ")
#     num2 = input ("Qual seu 2° numero: ")
    
#     if not num1.strip() or not num2.strip():
#         print("numero vazios, por favor digite algum numero")
#         continue
    
#     else: 
#         num1 = float(num1)
#         num2 = float(num2)
    
#     if escolha == "1":
#         print ("Escolha 1")
#         print (f"{num1} + {num2} = {num1+num2}")

#     elif escolha == "2":
#         print ("Escolha 2")
#         print (f"{num1} - {num2} = {num1-num2}")
    
#     elif escolha == "3":
#         print ("Escolha 3")
#         print (f"{num1} * {num2} = {num1*num2}")
    
#     elif escolha == "4":
#         print ("Escolha 4")
#         if num2 == 0:
#             print ("Seu numero 2 não pode ser 0 \n Por favor digite outro número.")
        
#         else:
#             print (f"{num1} / {num2} = {num1/num2}")
        

# if esporte != "1" or esporte != "2" or esporte != "3" or esporte != "4":
#         print ("Por favor, preencha o campo corretamente")
#         continue

# if esporte == "1":
#         print ("Você escolheu o futebol!")
#         print ("Nós precisamos de suas informações para a inscrição")
#         print ("==============")
        
#         nome = input ("Nome: ")
#         idade = input ("Idade: ")
#         email = input ("Email: ")
#         nivel = input ("Nível de escolaridade: ")
#         pos = input("Posição: ") 
#         doença = input ("Você tem alguma doença: ")
    
#     elif esporte == "2":
#         print ("Você escolheu o Voleibol!")
#         print ("Nós precisamos de suas informações para a inscrição")
#         print ("==============")
        
#         nome = input ("Nome: ")
#         idade = input ("Idade: ")
#         email = input ("Email: ")
#         nivel = input ("Nível de escolaridade: ")
#         pos = input("Posição: ") 
#         doença = input ("Você tem alguma doença: ")
    
    
#     elif esporte == "3":
#         print ("Você escolheu o banquete!")
#         print ("Nós precisamos de suas informações para a inscrição")
#         print ("==============")
        
#         nome = input ("Nome: ")
#         idade = input ("Idade: ")
#         email = input ("Email: ")
#         nivel = input ("Nível de escolaridade: ")
#         pos = input("Posição: ") 
#         doença = input ("Você tem alguma doença: ")
    
    
#     elif esporte == "4":
#         print ("Você escolheu o handebol!")
#         print ("Nós precisamos de suas informações para a inscrição")
#         print ("==============")
        
#         nome = input ("Nome: ")
#         idade = input ("Idade: ")
#         email = input ("Email: ")
#         nivel = input ("Nível de escolaridade: ")
#         pos = input("Posição: ") 
#         doença = input ("Você tem alguma doença: ")

# for i in range(3):
#     for j in range(3):
#         print (f"i: {i}, j: {j}")       


# for i in range(3):
#     for j in  range(i+1):
#         print ("*", end=" ")
#     print ()                          #quebra de linha 



# linha = int(input("escolha um numero base: "))


# for i in range(linha):
#     for j in  range(i+1):
#         print ("*", end=" ")
#     print ()     


# for i in range(3):
#     for j in range(2):
#         print(f"i:{i}, j:{j}")


# linha = int(input("escolha um numero: "))

# for i in range(linha):
#     for j in  range(i+1):
#         print (1+j, end=" ")
#     print ()     

# for i in range(0, 51):
#     if i %2 == 0: print (i)


# for i in range(1, 11):
#     print (i, end=" ")
# print ()     

# print ("====================")

# for i in reversed(range(1, 11)):
#     print (i, end=" ")
# print ()     

# print ("====================")

# for i in range(0 , 50, 2):
#     print (i, end=" " )
# print ()

# print ("====================")

# total=0
# for i in range (5):
#     num= float(input (f"digite o {i+1}º numero: "))
#     total += num
# print (total)


# print ("====================")

# num1 = int(input("qual tabuada voce quer ver ate o 10: "))
# for i in range(11):
#     print (f"{num1} X {i} = {num*i}")

# print ("====================")

# escolha = int(input("ate qual posicao da sequencia phi voce quer ver: "))

# nump = 0      
# nump1 = 1

# for i in range (escolha):
    
#     numph = nump + nump1
    
#     print (nump, end=" ")

#     nump=nump1
#     nump1=numph





# num = int(input("ate qual posicao da sequencia phi voce quer ver: "))
# a= 0
# b= 1
# for i in range (num):
#     print (a, end=", ")
#     proximo = a+b
#     a=b
#     b=proximo



# jogo de terminal repeticao, condicionaç
# pedra papel tesoura 
# escolha, escolha do comp aleatoria
# compara as escolhas
# atualizar pontuacao


# while True:
    

#     print ("=====================")
#     print ("Olá, seja benvindo ao jokenpo!")
#     print ("Para ganhar você precisará vencer 5 rodadas, o nosso esquema de pontos funciona da seguinte maneira:")
#     print ("Vitória: 1 ponto \nEmpate: 0 pontos \nPara vencer a partida: 5 pontos")
#     print ("=====================")
#     print (f"Digite 0 para sair \nDigite 1 para começar")

#     escolha = input("Digite aqui: ").strip()
    
#     if escolha == "0":
#         print ("Você saiu")
#         break
#     elif escolha == "1":
            
                  
            
            
#         #pontuacao
#         ponto_pc = 0
#         ponto_j = 0
        
#         while True:
            
#             #inicial
#             jogo = 0
#             pc = 0


#             if ponto_j == 5 or ponto_pc == 5:
                
#                 print ("==============")

#                 if ponto_j == 5:
#                     print ("Você ganhou!!")
#                 else:
#                     print ("O computador ganhou")

#                 print ("Você quer continuar jogando?")
#                 print ("Escolha 0 para sair \nEscolha 1 para continuar")
#                 fim = input("Sua escolha: ")
#                 if fim == "0":
#                     print ("Você saiu")
#                     break
#                 elif fim == "1":
#                     ("Vamos começar uma nova partida")
#                     continue

#                 else:
#                     print ("Escolha umas das opções dadas, tente novamente")
#                     continue
            
            
#             else:
#             #escolha jogador
#                 print ("=====================")
#                 print ("Para começar escolha entre:")
#                 print ("Pedra = 1 \nPapel = 2 \nTesoura = 3")
#                 jogo = input("Digite aqui: ").strip()
#                 print ("=====================")
                


#                 #escolha pc
#                 import random 
#                 pc = random.randint(1,3)
                
#                 #jogo
#                 if jogo == "1" and pc == 1:
#                     print ("Empate!")
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue
                
#                 if jogo == "2" and pc == 2:
#                     print ("Empate!")
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue
                
                
#                 if jogo == "3" and pc == 3:
#                     print ("Empate!")
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue

#                 #jogador ganha 
                
                
#                 elif jogo == "1" and pc == 3:
#                     print ("O jogador venceu a rodada!")    
#                     ponto_j += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 
                
#                 elif jogo == "2" and pc == 1:
#                     print ("O jogador venceu a rodada!")    
#                     ponto_j += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 
                
#                 elif jogo == "3" and pc == 2:
#                     print ("O jogador venceu a rodada!")    
#                     ponto_j += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 

                
#                 #pc ganha 

#                 elif pc == 1 and jogo == "3":
#                     print ("O computador venceu a rodada!")    
#                     ponto_pc += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 
                
#                 elif pc == 2 and jogo == "1":
#                     print ("O computador venceu a rodada!")    
#                     ponto_pc += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 
                
#                 elif pc == 3 and jogo == "2":
#                     print ("O computador venceu a rodada!")    
#                     ponto_pc += 1
#                     print ()
#                     print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                     continue 

#                 #escolha errada
                
#                 else:
#                     print ("Escolha umas das opções dadas, tente novamente")
#                     continue
            


#     else:
#         print ("=====================")
#         print ("Escolha umas das opções dadas, tente novamente")
#         continue








# print ("==============")
#             if ponto_j == 5:
#                 print ("Você ganhou!!")
#             else:
#                 print ("O computador ganhou")
#                 print ("Você quer continuar jogando?")
#                 print ("Escolha 0 para sair \nEscolha 1 para continuar")
#                 fim = input("Sua escolha: ")
#             if fim == "0":
#                 print ("Você saiu")
#                 break
#             elif fim == "1":
#                 ("Vamos começar uma nova partida")
#                 continue

#             else:
#                 print ("Escolha umas das opções dadas, tente novamente")
#                 continue

# while True:

#         #pontuacao
#     ponto_pc = 0
#     ponto_j = 0

#     print ("=====================")
#     print ("Olá, seja benvindo ao jokenpo!")
#     print ("Para ganhar você precisará vencer 5 rodadas, o nosso esquema de pontos funciona da seguinte maneira:")
#     print ("Vitória: 1 ponto \nEmpate: 0 pontos \nPara vencer a partida: 5 pontos")
#     print ("=====================")
#     print (f"Digite 0 para sair \nDigite 1 para começar")

#     escolha = input("Digite aqui: ").strip()
    
#     if escolha == "0":
#         print ("Você saiu")
#         break
#     elif escolha == "1":  
        
#         while ponto_j < 5 and ponto_pc <5:
            
#             #inicial
#             jogo = 0
#             pc = 0

#             #escolha jogador
#             print ("=====================")
#             print ("Para começar escolha entre:")
#             print ("Pedra = 1 \nPapel = 2 \nTesoura = 3")
#             jogo = input("Digite aqui: ").strip()
#             print ("=====================")
                


#                 #escolha pc
#             import random 
#             pc = random.randint(1,3)
                
#                 #jogo
#             if jogo == "1" and pc == 1:
#                 print ("Empate!")
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue
                
#             if jogo == "2" and pc == 2:
#                 print ("Empate!")
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue
                
                
#             if jogo == "3" and pc == 3:
#                 print ("Empate!")
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue

#                 #jogador ganha 
                
                
#             elif jogo == "1" and pc == 3:
#                 print ("O jogador venceu a rodada!")    
#                 ponto_j += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 
                
#             elif jogo == "2" and pc == 1:
#                 print ("O jogador venceu a rodada!")    
#                 ponto_j += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 
                
#             elif jogo == "3" and pc == 2:
#                 print ("O jogador venceu a rodada!")    
#                 ponto_j += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 

                
#                 #pc ganha 

#             elif pc == 1 and jogo == "3":
#                 print ("O computador venceu a rodada!")    
#                 ponto_pc += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 
                
#             elif pc == 2 and jogo == "1":
#                 print ("O computador venceu a rodada!")    
#                 ponto_pc += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 
                
#             elif pc == 3 and jogo == "2":
#                 print ("O computador venceu a rodada!")    
#                 ponto_pc += 1
#                 print ()
#                 print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
#                 continue 

#                 #escolha errada
                
#             else:
#                 print ("Escolha umas das opções dadas, tente novamente")
#                 continue
            
        


#         print ("==============")
#         if ponto_j == 5:
#             print ("Você ganhou!!")
#         else:
#             print ("O computador ganhou")
#             print ("Você quer continuar jogando?")
#             print ("Escolha 0 para sair \nEscolha 1 para continuar")
#             fim = input("Sua escolha: ")
#         if fim == "0":
#             print ("Você saiu")
#             break
#         elif fim == "1":
#             ("Vamos começar uma nova partida")
#             continue
#         else:
#             print ("Escolha umas das opções dadas, tente novamente")
#             continue


#     else:
#         print ("=====================")
#         print ("Escolha umas das opções dadas, tente novamente")
#         continue

# while True:

    #     #pontuacao
    # ponto_pc = 0
    # ponto_j = 0

    # print ("=====================")
    # print ("Olá, seja benvindo ao jokenpo!")
    # print ("Para ganhar você precisará vencer 5 rodadas, o nosso esquema de pontos funciona da seguinte maneira:")
    # print ("Vitória: 1 ponto \nEmpate: 0 pontos \nPara vencer a partida: 5 pontos")
    # print ("=====================")
    # print (f"Digite 0 para sair \nDigite 1 para começar")

    # escolha = input("Digite aqui: ").strip()
    
    # if escolha == "0":
    #     print ("Você saiu")
    #     break
    # elif escolha == "1":  
        
    #     while ponto_j < 5 and ponto_pc <5:
            
            
    #         #escolha jogador
    #         print ("=====================")
    #         print ("Para começar escolha entre:")
    #         print ("Pedra = 1 \nPapel = 2 \nTesoura = 3")
    #         jogo = input("Digite aqui: ").strip()
    #         print ("=====================")
                


    #             #escolha pc
    #         import random 
    #         pc = random.randint(1,3)
                
    #             #jogo


    #             #empate
    #         if jogo == "1" and pc == 1:
    #             print ("Empate!")
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue
                
    #         if jogo == "2" and pc == 2:
    #             print ("Empate!")
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue
                
                
    #         if jogo == "3" and pc == 3:
    #             print ("Empate!")
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue

    #             #jogador ganha 
                
                
    #         elif jogo == "1" and pc == 3:
    #             print ("O jogador venceu a rodada!")    
    #             ponto_j += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 
                
    #         elif jogo == "2" and pc == 1:
    #             print ("O jogador venceu a rodada!")    
    #             ponto_j += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 
                
    #         elif jogo == "3" and pc == 2:
    #             print ("O jogador venceu a rodada!")    
    #             ponto_j += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 

                
    #             #pc ganha 

    #         elif pc == 1 and jogo == "3":
    #             print ("O computador venceu a rodada!")    
    #             ponto_pc += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 
                
    #         elif pc == 2 and jogo == "1":
    #             print ("O computador venceu a rodada!")    
    #             ponto_pc += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 
                
    #         elif pc == 3 and jogo == "2":
    #             print ("O computador venceu a rodada!")    
    #             ponto_pc += 1
    #             print ()
    #             print (f"Jogador = {ponto_j} \nComputador = {ponto_pc}")
    #             continue 

    #             #escolha errada
                
    #         else:
    #             print ("Escolha umas das opções dadas, tente novamente")
    #             continue
            
        


    #     print ("==============")
    #     if ponto_j == 5:
    #         print ("Você ganhou!!")
    #     else:
    #         print ("O computador ganhou")
            
            
    #     print ("Você quer continuar jogando?")
    #     print ("Escolha 0 para sair \nEscolha 1 para continuar")
    #     fim = input("Sua escolha: ")
        
    #     if fim == "0":
    #         print ("Você saiu")
    #         break
    #     elif fim == "1":
    #         ("Vamos começar uma nova partida")
    #         continue
    #     else:
    #         print ("Escolha umas das opções dadas, tente novamente")
    #         continue


    # else:
    #     print ("=====================")
    #     print ("Escolha umas das opções dadas, tente novamente")
    #     continue



# lista = [10, 20, 30, 40]
# print (lista [2])

# numeros = [10, 20, 30, 40, 50]
# frutas = ["banana","kiwi", "jaca", "pitaya"]

# print (numeros[0])
# print (frutas[-1])

# frut = ["maca","banana", "laranja", "uva"]

# print (frut)
# print (frut[1])
# frut[1] = "manga"
# print (frut)
# print (frut[1])


# fruta = ["maca", "banana", "laranja"]

# fruta.append("abacaxi") #add um item no final
# fruta.remove("laranja") #tira um item 
# fruta.pop() #deleta o ultimo item
# fruta.insert("carambola") #add no inicio
# fruta.sort() #ordem alfabetica 
# fruta.reverse() #inverte a ordem

# print (fruta)

# print (lista([len(lista)-1]))      #len lista = o tamanho da lista (nao o indice)

# lista = []

# for i in range(1, 11):
#     lista.append(i)

# print (lista[0])
# print (lista[4])
# print (lista[-1])



# lista1 = [1,2,3,4,5,6,7,8,9,10]
# print (lista1[0,5,-1])

# lista1 = [0,1,2,3,4,5]
# lista2 = lista1.copy()

# print (lista2 [1:5:2])
# print ("=================")
# print (lista2 [::2])

# lista = []
# pares = []
# impares = []

# for i in range(100):
#     lista.append(i)

#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

# print (pares )
# print (impares )


# lista_par = (lista[::2])
# lista_impar = (lista[1::2])

# print (f"Lista par: {lista_par} \nLista impar: {lista_impar}")

# texto = 'abcdefg'
# for i in  (texto):
#     print (i, end=" ")

# print ()
# print (texto [0])

# nomes = ["ester","josias", "josefa", "adada"]
# for i, nome in enumerate (nomes):
#     print (f"{nome} - {i}")


# num = [1,2,3,4,5,6,7,8,9,10]

# print ("============")

# for i in num:
#     print (i, end = " ")

# print ()
# print ("============")

# for i in range (len(num)):
#     print (num[i], end = " ")

# print ()
# print ("============")

# for i, j in enumerate (num):
#     print (f"{i}, {j}")

# print ()
# print ("============")

# for i in range (len(num)):
#     num[i] = num[i]/2
# print (num)


# lista= [12,13,14,15]

# for i in range (len(lista)):
#     print (i)


# for i in range(len(num)):
#     print (num[i])


# num = [1,2,3,4,5,6,7,8,9,10]
# num2 = []



# for i in range (len(num)):
#     num2.append(num[i]*2)
# print (num)
# print (num2)


# numeros = [1, -2, -3, 4, 5, -6 , 7, -8, -9, 10]
# numeros1 = []

# for i in range (len(numeros)):
#     if numeros [i]>=0:
#         numeros1.append(numeros[i])
# print (numeros)
# print (numeros1)


# for i in range (len(numeros)):
#     numeros1.append(abs(numeros[i]))
# print (numeros)
# print (numeros1)

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print (matriz[0][2])
#       linha --- coluna

# for linha in matriz:
#     for coluna in linha:
#         print (j, end=" ")

# jogo = [
#     ["X", "O", "O"],
#     ["X", "X", "O"],
#     ["X", "O", "X"],
# ]

# for i in jogo:
#     for j in i:
#         print (f"[{j}]", end =" ")
#     print ()


# lista = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# somaLinha = []
# somaColuna = [0,0,0] 

# for i in lista:
#     soma = 0
#     for j in i:
#         soma+=j
#     somaLinha.append(soma)

# print (f"Soma das linhas: {somaLinha}")
        

# for i in lista:
#     soma=0
#     for indice, j in enumerate(i):
#         soma+= j
#         somaColuna[indice] += j
#         # print (indice)
#     somaLinha.append(soma)

# print (f"Soma das colunas: {somaColuna}")



##EUUUUUUUU

# nota = []
# soma = 0
# quant = random.randint(5,11)
# nota.sort()

# for i in range(quant):
#     num = random.uniform (0,10)
#     nota.append(round(num, 2))

# print (nota)

# print (f"A maior nota é: {nota[-1]}")
# print (f"A menor nota é: {nota[0]}")

# for i in nota:
#     soma += i
# print (f"A media das notas é: {round(soma / len(nota), 2)}")


# #METODO PROF

# notas = []

# for i in range (5):
#     numeroRandom = random.uniform(0, 10)
#     notas.append(round(numeroRandom, 2))

# print (notas)
# print (min(notas))
# print (max(notas))
# print (sum(notas)/len(notas))


# def mensagem():
#     print ("=====================")
#     print ("Olá tudo bem??")
#     print ("=====================")

# def dia():
#     hoje = date.today().day
#     print (hoje)

# mensagem()
# dia()


# print ("=====================")



# def areaCirculo():
#     raio = random.randint(1,20) 
#     area = math.pi * raio**2
#     print (f"raio = {raio}")
#     print (round(area, 2))

# areaCirculo()


# def mostrar_mens(nome, idade):
#     return f"ola {nome}, seu idade é {idade}"

# print(mostrar_mens("josefa", 85))


# while True:
#     def calculo(x, y, operacao):
#         match operacao:
#             case "adicao":
#                 return x+y
#             case "subtracao":
#                 return x-y
#             case "vezes":
#                 return x*y
#             case "divisao":
#                 if y ==0:
#                     return "Tenta dinovo porque deu ruim"
                
#                 return x/y

#             case default:
#                 return "operacao invalida"
        


#     operacao = input ("qual operacao voce quer (adicao, subtracao, multi, divisao): ")
#     X = input ("qual seu 1 numero: ")
#     y = input ("qual seu 1 numero: ")


#     try:
#         print (calculo(x, y, operacao))
#         break

#     except:
#         print ("deu erro ai, viu")
#         continue


# def soma (num1, num2):
#     soma = num1 + num2
#     return soma 

# print (soma(5,10))



# def parOuImpar(num):
#     if num%2== 0:
#         return "par"
#     return "impar"

# print (parOuImpar(64335764765756))

# def funcao(lista):
#     maximo = max(lista)
#     minimo = min(lista)

#     return (maximo, minimo)

# lista = [1,2,3,546,675,46,4,98765]


# print (funcao(lista))


# num1 =10
# num2 = 30
# def minha_funcao():
#     num2 = 20
#     print(num1, num2)

# print (num1, num2)    
# minha_funcao()


# #exercicio 1
# def soma(num1, num2):
#     return num1 + num2

# while True:
#     num1 = input("Primeiro numero: ")
#     num2 = input("Segundo numero: ")

#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         print (soma(num1, num2))

#     except:
#         print ("Escreva um numero seu jumento")
#         print("====================")
#         continue

#     break

# #exercicio 2
# def aprovado(nota):
#     if nota >=7:
#         return ("Aprovado, nao fez mais que sua obrigacao")
#     else:
#         return ("Reprovado, estude mais")

# while True:
#     nota = input("Qual sua nota (Escreva um numero de 0 a 10): ")

#     if nota < 0 or nota > 10:
#         print("Escreva um numero de 0 a 10")
#         continue

#     try:
#         nota = int(nota)
#         print (aprovado(nota))

#     except:
#         print ("Escreva um numero seu jumento")
#         print("====================")
#         continue

#     break

# #exercicio 1 / 3
# num1 = 0
# num2 = 0

# def ler():
#     num1 = int(num1)
#     num2 = int(num2)

# def soma(num1, num2):
#     return num1 + num2

# def resultado():
#     print (soma())

# while True:
#     num1 = input("Primeiro numero: ")
#     num2 = input("Segundo numero: ")

#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         soma(num1, num2)
#         resultado()

#     except:
#         print ("Escreva um numero seu jumento")
#         print("====================")
#         continue

#     break

# def soma(a,b):
#     return a+b

# print(soma(10,10))

# def aprovado(nota):
#     return "aprovado" if nota>=7 else "reprovado"

# print(aprovado(8))
# print(aprovado(4.5))

##########################

# def lerDados():
#     nome = input("seu nome: ")
#     idade = int(input("sua idade: "))

#     return (nome, idade)

# def processar(dados):
#     return f"Ola {dados[0]}, voce é maior de idade" if dados[1] >=18 else f"ola {dados[0]}, voce é menor de idade"

# def exibir(resultado):
#     print (resultado)


# resultado = processar(lerDados())
# exibir(resultado)

##########################

# def denovo():
#     while True:
#                     continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
#                     if continuar == "1":
#                         break
#                     elif continuar == "2":
#                         print("Muito obrigado por utilizar nossa calculadora.")
#                         exit()
#                     else:
#                         print("Valor inválido por favor responda com 1 ou 2.")

# def somar(num1, num2):
#     return f"{num1} + {num2} = {num1+num2}"

# def menos(num1, num2):
#     return f"{num1} - {num2} = {num1-num2}"

# def vezes(num1, num2):
#     return f"{num1} * {num2} = {num1*num2}"

# def dividir(num1, num2):
#     return f"{num1} / {num2} = {num1/num2}"

# print("=================")
# print ("Bem vindo a calculadora")
# print("=================")

# while True:

#     print ("Escolha entre: \n0 - sair \n1 - adicao \n2 - subtracao \n3 - multiplicacao \n4 - divisao")
#     escolha = input("digite aqui: ")
    
#     try:
#         escolha = int(escolha)
#     except:
#         print("escolha uma das opcoes")
#         print ("=================")
#         continue

#     num1 = input("Seu primeiro numero: ")
#     num2 = input("Seu segundo numero: ")
#     print ("=================")

#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#     except:
#         print("coloque numeros")
#         continue


#     match escolha:
#         case 0:
#             print("voce saiu")
            
#         case 1:
#             print(somar(num1, num2))
#             print ("=================")
#             denovo()
#             print ("=================")
            
#         case 2:
#             print(menos(num1, num2))
#             print ("=================")
#             denovo()
#             print ("=================")
            
#         case 3:
#             print(vezes(num1, num2))
#             print ("=================")
#             denovo()
#             print ("=================")
            
#         case 4:
#             if num2 == 0:
#                 ("seu segundo numero nao pode ser 0")
#                 continue
            
#             print(dividir(num1, num2))
#             print ("=================")
#             denovo()
#             print ("=================")
            
##########################

# def val_int(idade):
#     while True:
#         idade=input("Qual sua idade: ")
#         try:
#             idade = int(idade)
#         except:
#             print("digite um numero")
#             continue

# def name(nome):
#     while True:
#         nome=input("Qual seu nome: ").strip()
    
#         if nome =="":
#             return ("nome nao validado")
#             continue
#         else: 
#             return("nome validado")
        
# def year(idade):
#     while True:
#         idade=input("Qual sua idade: ")
#         if idade <1:
#             return "Sua idade deve ser maior de 0"
#         else:
#             return "Sua Idade é maior que 0"

# def senhaa(senha):
#     while True:
#         senha=input("Qual sua senha (numero max: 10 caracteres): ").strip()
    
#         if len(senha)>0 or len(senha) < 11:
#             return("senha validada")
            
#         else: 
#             return("senha nao validado")
#             continue





# print(val_int)
# print(year)
# print (senhaa)






# arrays 
# funcoes
# reoeticao
# decisao

# cadastro de usuario
# armazenar dados em arrays
# exibir informacoes
# controlar o fluxo


# nome idade e cidade

# lista1 = []
# lista = [1,2,3]
# lista1.append(lista)

# lista = [5,6,7]
# lista1.append(lista)


# print (lista1)



# upper() #tudo em maiusculo
# lower() #tudo em minusculo
# strip() #retira espaço
# split() #divide em uma lista, divde pelo espaço
# join() #junta partes em uma str
# len() #retorna o tamanho da lista/texto
# in #se contem texto ou algo
# startwith() #verifica o inicio do texto                boolean
# endswith() #verifica o final                           boolean



# texto = "Eu gosto de maça"

# print(texto.split(" "))
# print ("-".join(texto.split(" ")))

# print(texto.upper())
# print(texto.lower())
# print(texto.strip())
# print(len(texto))
# print(len(texto..strip()split(" ")))

# def nome():
#     while True:
#         nome = input("Nome: ").replace(" ", "")
#         if nome == "" or not nome.isalpha():
#             print ("Deu ruim")
#             print ("tente denovo")

#         else:
#             nome = nome.lower()
#             nome = nome[0].upper() + nome[1:]  #capitalize
#             print (nome)
#             break


# def senha():
#     while True:
#         print ()
#         senha = input("Senha: ").replace(" ", "")

#         letra = any(caracter.isalpha() for caracter in senha)
#         num = any(caracter.isdigit() for caracter in senha)
#         carac = any(not caracter.isalnum() for caracter in senha)

#         if len(senha) > 10 or len(senha) < 1:
#             print("Coloque menos de 10 valores")
#             continue
            


#         if letra and num and carac:
#             print("senha valida")
#             break
#         else:
#             print ("=================")
#             if not letra:
#                 print ("precisa de letra")
                
#             if not num:
#                 print ("precisa de numero")
                
#             if not carac:
#                 print ("precisa de caracter especial")
            
#             print ("tente denovo")

# def contar():
#     while True:
#         texto = input("Digite seu texto: ")

#         letras = len(texto.replace(" ", ""))
#         palavras = len(texto.split(" "))
#         a = input ("que palavra vc gostaria de verificar: ")
#         verificar = texto.lower().split().count(a.lower())


#         print(f"quantidade de letras = {letras}")
#         print(f"quantidade de palavras = {palavras}")
#         print(f"Sua palavra aparece {verificar} vezes")

#         break


# nome()
# senha()
# contar()


# letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# texto = input("Qual sua palavra: ").replace(" ", "")
# casa = int(input("Qual o numero de casas do deslocamento: "))

# novo_texto = ""

# for i in texto:
#     letra = letras.index(i)
#     nova_letra = letras[(letra + casa) % 26]
#     novo_texto += nova_letra

# print(novo_texto)


ligar arquivos

