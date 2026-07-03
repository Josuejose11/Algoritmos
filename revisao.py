# # 1
# numero = int(input("escolha um numero: "))
# if numero>0:
#     print ("Seu numero é positivo")
# elif numero==0:
#     print ("O seu numero é 0")
# elif numero<0:
#     print ("o seu numero é negativo")

# #2
# idade = int(input("Qual a sua idade? "))
# if idade>0 and idade<4:
#     print ("Você é um bebe")
# elif idade>=4 and idade<=12:
#     print ("Você é uma criança")
# elif idade>12 and idade<18:
#     print ("Você é um adolescente")
# elif idade>=18 and idade<60:
#     print ("Você é um adulto")
# #3
# nota = float(input("Qual a sua nota: "))
# if nota>6 and nota<=10:
#     print ("Você esta aprovado")
# elif nota>3 and nota<7:
#     print ("Você esta de recuperacao")
# elif nota<4 and nota>0:
#     print ("Você esta reprovado")

# #4
# num = int(input("Escolha um numero: "))
# num_novo = num.replace (" ", "")
# print("é par" if num % 2 == 0 else "é impar")

#5
senha = (input("qual sua senha: ")).strip
if not senha:
    print ("a senha nao pode estar vazia")
elif len(senha) < 8:
    print ("a senha deve conter menos de 8 caracteres")
else:
    print ("senha invalida")

# senha_nova = senha.replace (" ", "")
# if senha_nova == "":
#     print ("sua senha nao esta validada")
# else:
#     print ("sua senha esta validada")


#6

import random

num2 = random.randint(1,100)
num1 = int(input("escolha um numero de 1 a 100: "))

while num1 != num2:
    if num2>num1:
        num1 = int(input("Você errou, o número escolhido é maior, escolha outro numero de 1 a 100: "))
    else:
        num1 = int(input("Você errou, o número escolhido é menor, escolha outro numero de 1 a 100: "))

if num1 == num2:
    print ("voce acertou o numero")

#7

valor = float(input("Valor da compra: "))

if valor <= 100:
    valorSD = valor
    print ("nenhum desconto aplicado")
    print(f"Valor final: {valorSD}")
elif valor > 100 and valor <300:
    valorCD1 = valor *90/100
    print ("desconto de 10% aplicado")
    print(f"Valor final: {valorCD1}")
elif valor >300:
    valorCD2 = valor*80/100
    print ("desconto de 20% aplicado")
    print(f"Valor final: {valorCD2}")

