# print("Olá seja bem-vindo a calculadora!")
# operacao = input("Para começar escolha qual operação você usará (+, -, *, / e **): ")
# num1 =  float(input ("Qual o primeiro número que você irá usar? "))
# num2 = float(input ("Qual o segundo número que você irá usar? "))

# # numero = numero1.replace (" ", "")

# if not operacao.strip() == "":
#     print("Você não preencheu o campo, por favor tente novamente.")

# if not num1.strip() or num2.strip() == "":
#     print ("O Campo de numero esta vazio")

# #

# if operacao == "+":
#     print (f"{num1} + {num2} = {num1+num2}")

# elif operacao == "-":
#     print (f"{num1} - {num2} = {num1-num2}")

# elif operacao == "*":
#     print (f"{num1} * {num2} = {num1*num2}")

# elif operacao == "/":
#     if num2==0:
#         print("Seu divisor não pode ser 0, tente novamente")
#     else:
#         print (f"{num1} / {num2} = {num1/num2}")

# elif operacao == "**":
#     print (f"{num1} ** {num2} = {num1**num2}")
    

# else:
#     print ("Por favor, preencha o campo corretamente.")

while True:
    print ("================== \nBem vindo a calculdora!! \nEscolha uma opção. \n==================")
    print ("0 - sair")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")

    escolha = input()
    if escolha == "0":
        print ("Você saiu")
        break
    

    
    
    if escolha == "0" or escolha =="1" or escolha =="2" or escolha =="3" or escolha =="4":
        num1 = input ("Qual seu 1° numero: ")
        num2 = input ("Qual seu 2° numero: ")
        
        if not num1.strip() or not num2.strip():
            print("numero vazios, por favor digite algum numero")
            continue
        
        else: 
            num1 = float(num1)
            num2 = float(num2)
        
        if escolha == "1":
            print ("Escolha 1")
            print (f"{num1} + {num2} = {num1+num2}")
            
            print ("================== \nVocê gostaria de fazer outro calculo? \n0 - Não, sair \n1 - Sim, fazer outro calculo")

            fim = input()
            
            if fim == 0:
                print ("Você saiu")
                break
            else:
                continue

        elif escolha == "2":
            print ("Escolha 2")
            print (f"{num1} - {num2} = {num1-num2}")
            
            print ("================== \nVocê gostaria de fazer outro calculo? \n0 - Não, sair \n1 - Sim, fazer outro calculo")

            fim = input()
            
            if fim == 0:
                print ("Você saiu")
                break
            else:
                continue
        
        elif escolha == "3":
            print ("Escolha 3")
            print (f"{num1} * {num2} = {num1*num2}")
            
            print ("================== \nVocê gostaria de fazer outro calculo? \n0 - Não, sair \n1 - Sim, fazer outro calculo")

            fim = input()
            
            if fim == 0:
                print ("Você saiu")
                break
            else:
                continue
        
        elif escolha == "4":
            print ("Escolha 4")
            if num2 == 0:
                print ("Seu numero 2 não pode ser 0 \n Por favor digite outro número.")
            
            else:
                print (f"{num1} / {num2} = {num1/num2}")
                
                print ("================== \nVocê gostaria de fazer outro calculo? \n0 - Não, sair \n1 - Sim, fazer outro calculo")

            fim = input()
            
            if fim == 0:
                print ("Você saiu")
                break
            else:
                continue

    else:
        print ("Você não escolheu uma opção \nEscolha uma das alternativas ")
        