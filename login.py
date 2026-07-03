#lista de cadastros gerais
cadastros = []

#def mensagem inicial
def mensagem():
    print ("=================")
    print ("Seja bem vindo(a) ao nosso sistema de cadastros!!")
    print ("=================")

#def fazer denovo
def denovo():
    while True:
        print ("=================")
        continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
        if continuar == "1":
            break
        elif continuar == "2":
            print("Muito obrigado por utilizar nossa sistema de cadastro.")
            exit()
        else:
            print("Valor inválido por favor responda com 1 ou 2.")
        
        print ("=================")

#def erro
def erro():
    print (f"------------")
    print (f"*Ocorreu um erro, tente novamente*")
    print (f"------------")
    
#def ler usuarios
def ler_usuarios(cadastros):
    for i, j in enumerate(cadastros):
        print(f"Id: {i} | Nome: {j[0]} | Idade: {j[1]} | Cidade: {j[2]}")

#def validacao de idade
def validacao_idade():
    while True:
        idade = input("Sua idade: ")
        
        try:
            idade = int(idade)
        except:
            print("Coloque sua idade corretamente")
            continue

        if idade < 0:
            print ("Idade incompativel, tente novamente")
            continue
        
        return idade
        # break

# def validacao do nome e cidade = int, ""
def validacao_nome_cidade(nome, cidade):
    if nome == "" or cidade =="":
        return False
    
    if nome.isdigit() or cidade.isdigit():
        return False
    return True
    
#def cadastrar usuarios
def cadastrar_usuarios(nome, idade, cidade):
    cadastros.append([nome, idade, cidade])

#boas vindas
mensagem()

while True:

    #sistema
    print("Escolha uma das opções abaixo:")
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Ver usuários")
    escolha = input("Escreva aqui: ")
    print ("=================")

    #validar escolha
    match escolha:
        case "0":
            print ("Voce saiu")
            break
        
        case "1":
            while True:
                print("Para cadastrar precisaremos de algumas informações suas.")
                nome = input("Seu nome: ").strip()
                idade = validacao_idade()
                cidade = input("Sua cidade: ").strip()

                if not validacao_nome_cidade(nome, cidade):
                    erro()
                    continue
                else:
                    cadastrar_usuarios(nome, idade, cidade)
                    ler_usuarios(cadastros)

                    print ("Cadastro feito com sucesso!")
                    break

            denovo()
                
        case "2":
            ler_usuarios(cadastros)
            denovo()
            




