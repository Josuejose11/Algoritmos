# Script SQL

# CREATE DATABASE IF NOT EXISTS biblioteca_db;

# USE biblioteca_db;


# CREATE TABLE IF NOT EXISTS  autores (

#     id_autor INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     nacionalidade VARCHAR(50)
# );

# CREATE TABLE IF NOT EXISTS livros (

#     id_livro INT AUTO_INCREMENT PRIMARY KEY,
#     titulo VARCHAR(150) NOT NULL,
#     ano_publicacao INT,
#     fk_id_autor INT,
#     FOREIGN KEY (fk_id_autor) REFERENCES autores(id_autor)
# );










#   if resultado:
#         senha()
#     else:
#         print ()



#Importa o mysql para fazer essa ligacao
import mysql.connector
from mysql.connector import Error

#def fazer denovo

def denovo():
    while True:
                    continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
                    if continuar == "1":
                        break
                    elif continuar == "2":
                        print("Muito obrigado por utilizar nossa biblioteca.")
                        exit()
                    else:
                        print("Valor inválido por favor responda com 1 ou 2.")

#def erro
def erro():
    print (f"------------")
    print (f"*Ocorreu um erro, tente novamente*")
    print (f"------------")
    
#conecta com o sql e o banco de dados em especifico

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database ='biblioteca_db'
        )
        return conexao
    except Error as e:
        print (f"Erro ao conectar ao mySql: {e}")
        return None

# CREATE / CRIAR - cria categorias, ex.: usuarios

def criar_autor (nome, nacionalidade):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO autores (nome, nacionalidade) VALUES (%s, %s)"
    valores = (nome, nacionalidade)
    cursor.execute(sql, valores)
    conn.commit()    

    print (f"{cursor.rowcount} registro(s) inserido(s).")
    cursor.close()
    conn.close()

def criar_livros(titulo, ano_publicacao, fk_id_autor):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO livros (titulo, ano_publicacao, fk_id_autor) VALUES (%s, %s, %s)"
    valores = (titulo, ano_publicacao, fk_id_autor)
    cursor.execute(sql, valores)
    conn.commit()    
    
    print (f"{cursor.rowcount} registro(s) inserido(s).")
    print ("=================")     
    print("Ok tudo certo, adicionamos as informações sobre seu livro com sucesso.")
    print ("=================")    
    cursor.close()
    conn.close()
  
# READ / LER - lê e entendende o que foi inserido - define o read

def ler_autores():

    print ("=================")

    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM autores")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"ID: {linha[0]} | nome: {linha[1]} | nacionalidade: {linha[2]}")

    cursor.close()
    conn.close()

    return ("=================")

def ler_livros():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    print ("=================")
    query = """
        SELECT livros.titulo, autores.nome
        FROM livros
        INNER JOIN autores
            ON livros.fk_id_autor
            = autores.id_autor
        """
    
    cursor.execute(query)
    resultado = cursor.fetchall()

    for titulo, autor in resultado:
        print(f"{titulo} — {autor}")



    cursor.close()
    conn.close()
    
    print ("=================")

def ler_livros_total():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM livros")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"ID: {linha[0]} | titulo: {linha[1]} | ano de publicação: {linha[2]}")

    cursor.close()
    conn.close()

# UPDATE / ATUALIZAR - atualiza informacoes ja cadastradas - define o update

def atualizar_autor(id_autor, nome, nacionalidade):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = (f"UPDATE autores SET nome = %s, nacionalidade = %s WHERE id_autor = %s")
    valores = (nome, nacionalidade, id_autor)

    cursor.execute(sql, valores)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) atualizado(s).")
    cursor.close()
    conn.close()

def atualizar_livros(id_livro, novo_x):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = (f"UPDATE livros SET {novo_x} = %s WHERE id_livro = %s")
    valores = (novo_y, id_livro)

    cursor.execute(sql, valores)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) atualizado(s).")
    cursor.close()
    conn.close()

# DELETAR - deleta certa escolha - define o delete

def deletar_autor(id_autor): 
    
    
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = ("DELETE FROM autores WHERE id_autor = %s")
    valor = (id_autor,)

    cursor.execute(sql, valor)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) apagado(s).")
    cursor.close()
    conn.close()    
    
def deletar_livros(id_livro): 
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = ("DELETE FROM livros WHERE id_livro = %s")
    valor = (id_livro,)

    cursor.execute(sql, valor)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) apagado(s).")
    cursor.close()
    conn.close()



# DATABASE biblioteca

print ("=================")
print ("Seja bem vindo(a) a nossa biblioteca virtual!!")
print ("Aqui voce podera cadastrar seus livros")
print ("=================")



while True:
    
    #Define as opcoes
    opcoes = ["0", "1", "2", "3", "4"]


    #Escolha usuario

    print ("Em qual categoria você gostaria de mecher?")
    print ("0 - Sair ")
    print ("1 - autor")
    print ("2 - livros")

    print("------------")

    a = input("Escolha aqui: ")

    print("------------")
    
    if not a in opcoes [:3]:
        print("Opção inválida")
        continue

    elif a == "0":
        print ("Voce saiu")
        break

    #autores

    elif a == "1":
        print ("Digite o que voce gostaria de fazer, sabendo que podera mexer no autor e nacionalidade")
        print ("0 - Sair ")
        print ("1 - Adicionar")
        print ("2 - Atualizar")
        print ("3 - Deletar")
        print ("4 - Vizualizar")
        
        escolha = input("digite aqui: ")

        match escolha:
            case "0":
                print ("Voce saiu")
                break
            case "1":
                while True: 

                    nome = input("Nome do autor: ")
                    nacionalidade = input(f"Qual a nacionalidade do(a) autor(a) {nome}: ")
                    
                    try:
                        criar_autor (nome, nacionalidade)
                        #mensagem
                        print ("=================")     
                        print("Ok tudo certo, adicionamos as informações sobre seu livro com sucesso.")
                        print ("=================")     
                        # Read
                            
                        ler_autores()
                        print ("=================")   

                        break   
                    except:
                        erro()
                        continue

                #Caso queira fazer denovo ou sair
                denovo()

            case "2":
                while True: 
                    
                    ler_autores()

                    id_autor = input ("Id do autor que você irá alterar: ")
                    nome = input("Nome do autor: ")
                    nacionalidade = input(f"Qual a nacionalidade do(a) autor(a) {nome}: ")

                    try:
                        id_autor = int(id_autor)
                    except:
                        print (f"Ocorreu um erro no Id, tente novamente")
                        continue
                    
                    try:
                        atualizar_autor (id_autor, nome, nacionalidade)
                        #mensagem
                        print ("=================")     
                        print("Ok tudo certo, adicionamos as informações sobre seu autor com sucesso.")
                        print ("=================")     
                        # Read
                            
                        ler_autores()
                        print ("=================")   

                        break   
                    except:
                        erro()
                        continue

                #Caso queira fazer denovo ou sair
                denovo()

            case "3":
                while True:

                    ler_autores()
                    print ("Qual autor você gostaria de excluir?")
                    id_autor = input ("Digite aqui: ")
                    deletar_autor(id_autor)
                    ler_autores()
                
                    #mensagem
                    print ("=================")
                    print ("Livro deletado com sucesso!!")
                    print ("=================")

                    #Caso queira fazer denovo ou sair
                    denovo()

            case "4":

                print (ler_autores())
                denovo()

    #livros

    else:
        print ("Digite o que voce gostaria de fazer, sabendo que podera mexer no livro e ano e publicaco")
        print ("0 - Sair ")
        print ("1 - Adicionar")
        print ("2 - Atualizar")
        print ("3 - Deletar")
        print ("4 - Vizualizar")
        
        escolha1 = input("digite aqui: ")

        match escolha1:
            case "0":
                print ("Voce saiu")
                break
            case "1":
                while True: 
                    
                    print(ler_autores())

                    fk_id_autor = input("Id do autor: ")
                    titulo = input("Nome do livro: ")
                    ano_publicacao = input(f"Qual o ano de publicação do livro {titulo}: ")
                    
                    try: 
                        fk_id_autor = int(fk_id_autor)
                    except:
                        print("Ocorreu um erro no id autor, tente novamente")
                        continue

                    try:
                        criar_livros (titulo, ano_publicacao, fk_id_autor)
                        # Read
                            
                        ler_livros_total()
                        print ("=================")   

                        break   
                    except:
                        erro()
                        continue

                #Caso queira fazer denovo ou sair
                denovo()

            case "2":
                while True: 
                    print ("=================")     
                    print ("O que você gostaria de alterar no livro?")
                    print ("0 - Sair")
                    print ("1 - Título")
                    print ("2 - Ano de publicação")

                    novo_x = input("Escreva aqui: ")
                    print ("=================")     

                    ler_livros_total()

                    id_livro = input ("Id do livro que você irá alterar: ")

                    try:
                        print ("=================")     
                        id_livro = int(id_livro)
                        print ("=================")  

                    except:
                        erro()
                        continue

                    #define a variavel que o usuario vai mudar

                    match novo_x:
                        case "0":
                            print ("Voce saiu")
                            break
                        case"1":
                            novo_y = input("Qual seu novo título: ")
                            novo_x = "titulo"
                        case"2":
                            novo_y = input("Qual seu novo ano de publicação: ")
                            novo_x = "ano_publicacao"
                        case _:
                            print("Opção inválida")
                            continue

                    try:
                        atualizar_livros (id_livro, novo_x)
                        #mensagem
                        print ("=================")     
                        print("Ok tudo certo, adicionamos as informações sobre seu autor com sucesso.")
                        print ("=================")     
                        # Read
                            
                        ler_livros_total()
                          
                        

                        break   
                    except:
                        erro()
                        continue

                #Caso queira fazer denovo ou sair
                denovo()

            case "3":
                while True:

                    ler_livros_total()
                    print ("Qual o id do livro você gostaria de excluir?")
                    id_livro = input ("Digite aqui: ")

                    try:
                        print ("=================")     
                        id_livro = int(id_livro)
                        print ("=================")  
                    except:
                        erro()
                        continue

                    try:
                        deletar_livros(id_livro)
                        ler_livros()
                        break
                    except:
                        erro()
                        continue

                    #mensagem
                    print ("=================")
                    print ("Livro deletado com sucesso!!")
                    print ("=================")

                    #Caso queira fazer denovo ou sair
                    denovo()

            case "4":

                print (ler_livros())
                denovo()
                print ("=================")

            case _:
                erro()
                continue
