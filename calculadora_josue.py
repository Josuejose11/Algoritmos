# print("Olá seja bem-vindo a calculadora!")
# numero1 = input("Para começar escolha qual operação você usará (adição, subtração, multiplicação, divisão e potência): ")
# numero = numero1.replace (" ", "")

# if numero == "":
#     print("Você não preencheu o campo, por favor tente novamente.")


# if numero == "adição":
#     num1 = float (input ("Qual o primeiro número que você irá somar? "))
#     num2 =float (input ("Qual o segundo número que você irá somar? "))
#     print (f"{num1} + {num2} = {num1+num2}")

# elif numero == "subtração":
#     num3 = float (input ("Qual o primeiro número que você irá subtrair? "))
#     num4 =float (input ("Qual o segundo número que você irá subtrair? "))
#     print (f"{num3} - {num4} = {num3-num4}")

# elif numero == "multiplicação":
#     num5 = float (input ("Qual o primeiro número que você irá multiplicar? "))
#     num6 =float (input ("Qual o segundo número que você irá multiplicar? "))
#     print (f"{num5} * {num6} = {num5*num6}")

# elif numero == "divisão":
#     num7 = float (input ("Qual o número que irá ser dividido? "))
#     num8 =float (input ("Qual o número que irá ser o divisor? "))
#     if num8==0:
#         print("Seu divisor não pode ser 0, tente novamente")
#     else:
#         print (f"{num7} / {num8} = {num7/num8}")

# elif numero == "potência":
#     num9 = float (input ("Qual o número de sua base da potência? "))           
#     num10 =float (input ("Qual o número que irá ser o expoênte? "))
#     print (f"{num9} ** {num10} = {num9**num10}")

# else:
#     print ("Por favor, preencha o campo corretamente.")


print("Olá seja bem-vindo a calculadora!")
numero1 = input("Para começar escolha qual operação você usará (adição, subtração, multiplicação, divisão e potência): ")
numero = numero1.replace (" ", "")

match numero:
    case "adição":
        num1 = float (input ("Qual o primeiro número que você irá somar? "))
        num2 =float (input ("Qual o segundo número que você irá somar? "))
        print (f"{num1} + {num2} = {num1+num2}")

    case "subtração":
        ...
    case "multiplicação":
        ...
    case "divisão":
        ...
    case "potência":
        ...        







