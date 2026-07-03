#SCRIPSQL

# CREATE DATABASE IF NOT EXISTS loja;

# USE loja;

# CREATE TABLE IF NOT EXISTS clientes(
#     id_clientes INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL, 
#     email VARCHAR (100) UNIQUE,
#     senha VARCHAR (100) 
#     );
    
# CREATE TABLE IF NOT EXISTS pedidos(
# 	id_pedidos INT auto_increment primary KEY,
#     pedido VARCHAR (100),
#     valor FLOAT,
# 	fk_id_clientes INT,
#     FOREIGN KEY (fk_id_clientes) REFERENCES clientes(id_clientes)
#     );
    
# SELECT*FROM clientes;



#Importa o mysql para fazer essa ligacao
import mysql.connector
from mysql.connector import Error

#opçoes
opcoes = ["0", "1", "2", "3"]

#def fazer denovo
def denovo():
    while True:
        print("=================")
        continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
        if continuar == "1":
            break
        elif continuar == "2":
            print("Muito obrigado por utilizar nossa loja.")
            exit()
        else:
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")

#conecta com o sql e o banco de dados em especifico
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database ='loja'
        )
        return conexao
    except Error as e:
        print (f"Erro ao conectar ao mySql: {e}")
        return None

#def erro
def erro():
    print (f"------------")
    print (f"*Ocorreu um erro, tente novamente*")
    print (f"------------")

#validacao de id
def senha_(id_clientes, senha):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM clientes WHERE id_clientes = %s AND senha = %s"
    valores = (id_clientes, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()   
    
    cursor.close()
    conn.close()

    if not resultado:
        print (f"------------")
        print("Senha não encontrada")
        print (f"------------")
        return False
    else:
        return True
    
#criar / create
def criar_clientes(nome, email, senha):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    conn.commit()    
    print (f"------------")
    print (f"{cursor.rowcount} usuário cadastrado.")
    print (f"------------")
    cursor.close()
    conn.close()

#ler / read
def ler_clientes():

    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute("SELECT*FROM clientes")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"ID: {linha[0]} | nome: {linha[1]} | email: {linha[2]}")

    cursor.close()
    conn.close()

    print ("=================")

def ler_pedidos():
    conn = criar_conexao()
    cursor = conn.cursor()

    sql = """
    SELECT clientes.nome, SUM(pedidos.valor)
    FROM pedidos
    INNER JOIN clientes
        ON pedidos.fk_id_clientes = clientes.id_clientes
    WHERE clientes.id_clientes = %s
    """

    cursor.execute(sql, (id_clientes,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado is None or resultado[1] is None:
        print("=================")
        print("Nenhuma compra encontrada.")
        print("=================")
        return

    nome, total = resultado

    print("=================")
    print(f"Cliente: {nome}")
    print(f"Total gasto: R$ {total:.2f}")
    print("=================")

#deletar clientes
def deletar_clientes(id_clientes):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        sql = "DELETE FROM clientes WHERE id_clientes = %s"
        cursor.execute(sql, (id_clientes,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Nenhum usuário encontrado.")
        else:
            print("Usuário deletado com sucesso.")

    except Error as e:
        print("------------")
        print("Não é possível deletar: cliente possui pedidos vinculados.")
        print("------------")

    finally:
        cursor.close()
        conn.close()

#def comprar
def comprar(pedido, valor, id_clientes):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO pedidos (pedido, valor, fk_id_clientes) VALUES (%s, %s, %s)"
    valores = (pedido, valor, id_clientes)
    cursor.execute(sql, valores)
    conn.commit()    
    
    cursor.close()
    conn.close()
    
    print("Compra realizada com sucesso!")
    print ("=================")

#def verificacao
def verificacao(nome, email, senha):
    if nome.isdigit():
        return False
    if nome.strip() == "" or email.strip() == "" or senha.strip() == "":
        return False

    return True


#sistema principal
print("=================")
print ("Seja bem vindo a nossa loja!!")
print("=================")

while True:
    print ("Você já tem login? \n0 - Sair \n1 - sim \n2 - Não")
    login = input("Escreva aqui: ")
    print("=================")
    

    #validacao
    if not login in opcoes[:3]:
        print("Selecione uma das opções.")
        continue

    #sair
    elif login == opcoes[0]:
        print("Você saiu, volte sempre!!")
        break

    #entrar
    elif login == opcoes[1]:
        print("Vamos entrar na sua conta.")
        print("=================")  

        while True:
            ler_clientes()

            try:
                id_clientes = int(input("Qual o id da sua conta: ").strip())
            except:
                erro()
                continue
            
            
            senha = input("Qual sua senha: ").strip()
            
            #validacao espaco vazio
            if id_clientes =="" or senha =="":
                erro()
                continue
            
            
            #validacao da senha 
            validacao1 = senha_(id_clientes, senha)

            if not validacao1:
                continue
            else:
                print("Senha válida")
                print ("Você entrou.")
                print("=================") 

            while True:
                #opcoes
                print("O que voce gostaria de fazer?")
                print("0 - Sair")
                print("1 - Comprar")
                print("2 - Ver extrato de vendas")
                print("3 - Deletar usuário")
                escolha = input("Escreva aqui: ")
                print("=================") 

                match escolha:
                    case "0":
                        print("Você saiu, volte sempre!!")
                        exit()
                    case "1":
                        #aba de compra
                        print("Qual item você gostaria de comprar?")
                        print("0 - Sair")
                        print("1 - Brinquedos")
                        print("2 - Roupas")
                        escolha = input("Escreva aqui: ")
                        print("=================") 

                        match escolha:
                            case "0":
                                print("Você saiu, volte sempre!!")
                                exit()

                            case "1":
                                print("Temos diversas opções de brinquedos, escolha uma:")
                                print("0 - Sair")
                                print("1 - Carrinhos -- R$ 10,00")
                                print("2 - Bonecas -- R$ 15,00")
                                print("3 - Trenzinhos -- R$ 8,00")
                                escolha = input("Escreva aqui: ")
                                print("=================") 

                                match escolha:
                                    case "0":
                                        print("Você saiu, volte sempre!!")
                                        exit()
                                    case "1":
                                        pedido = "carrinhos"
                                        valor = 10
                                        comprar(pedido, valor, id_clientes)
                             

                                    case "2":
                                        pedido = "bonecas"
                                        valor = 15
                                        comprar(pedido, valor, id_clientes)


                                    case "3":
                                        pedido = "trenzinhos"
                                        valor = 8
                                        comprar(pedido, valor, id_clientes)
                                        

                                ler_pedidos()
                                denovo()

                            case "2":
                                print("Temos diversas opções de roupas, escolha uma:")
                                print("0 - Sair")
                                print("1 - Bermudas -- R$ 10,00")
                                print("2 - blusas -- R$ 15,00")
                                print("3 - moletons -- R$ 8,00")
                                escolha = input("Escreva aqui: ")
                                print("=================") 

                                match escolha:
                                    case "0":
                                        print("Você saiu, volte sempre!!")
                                        exit()
                                    case "1":
                                        pedido = "bermudas"
                                        valor = 10
                                        comprar(pedido, valor, id_clientes)


                                    case "2":
                                        pedido = "blusas"
                                        valor = 15
                                        comprar(pedido, valor, id_clientes)
    

                                    case "3":
                                        pedido = "moletons"
                                        valor = 8
                                        comprar(pedido, valor, id_clientes)

                                
                                ler_pedidos()
                                denovo()

                            case _:
                                print("Escreva uma das opções dadas.")
                                continue

                    case "2":
                        ler_pedidos()
                        denovo()

                    case "3":
                        deletar_clientes(id_clientes)
                        denovo()

                    case _:
                        print("Digite uma das opções dadas")

    #criar conta
    elif login == opcoes[2]:
        print ("Vamos criar sua conta!")
        print("=================")  
        while True:
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
        
            if not verificacao(nome, email, senha):
                erro()
                continue

            try:
                criar_clientes(nome, email, senha)
                print ("Conta criada com sucesso!!")
                print("=================")  
                break

            except:
                print (f"------------")
                print("Ocorreu um erro com a sua validação, tente novamente.")
                print (f"------------")
                continue

    else:
        erro()
        continue

