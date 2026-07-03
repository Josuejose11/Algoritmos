# Script SQL
 
# CREATE DATABASE IF NOT EXISTS biblioteca;
# USE biblioteca;
 
# CREATE TABLE IF NOT EXISTS livros(
# id INT AUTO_INCREMENT PRIMARY KEY,
# titulo VARCHAR(100) NOT NULL,
# autor VARCHAR (100) NOT NULL,
# ano_de_lancamento DATE
# );
# SELECT*FROM livros;
 
# truncate table livros;
# -- drop table livros;


#Importa o mysql para fazer essa ligacao
import mysql.connector
from mysql.connector import Error


#conecta com o sql e o banco de dados em especifico

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database ='biblioteca'
        )
        return conexao
    except Error as e:
        print (f"Erro ao conectar ao mySql: {e}")
        return None

# CREATE / CRIAR - cria categorias, ex.: usuarios

def criar_livros(titulo, autor, ano_de_lancamento):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO livros (titulo, autor, ano_de_lancamento) VALUES (%s, %s, %s)"
    valores = (titulo, autor, ano_de_lancamento)
    cursor.execute(sql, valores)
    conn.commit()    

    print (f"{cursor.rowcount} registro(s) inserido(s).")
    cursor.close()
    conn.close()
   
# READ / LER - lê e entendende o que foi inserido - define o read

def ler_livros():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM livros")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"ID: {linha[0]} | titulo: {linha[1]} | autor: {linha[2]} | data_de_lancamento: {linha[3]}")

    cursor.close()
    conn.close()

# UPDATE / ATUALIZAR - atualiza informacoes ja cadastradas - define o update

def atualizar_livros(idd, novo_x):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = (f"UPDATE livros SET {novo_x} = %s WHERE id = %s")
    valores = (novo_y, idd)

    cursor.execute(sql, valores)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) atualizado(s).")
    cursor.close()
    conn.close()

# DELETAR - deleta certa escolha - define o delete

def deletar_livros(id_livros): 
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = ("DELETE FROM livros WHERE id = %s")
    valor = (id_livros,)

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
    opcao = ["0", "1", "2", "3", "4"]


    #Escolha usuario

    print ("O que voce gostaria de acrescentar? ")
    print ("Digite o que voce gostaria de fazer, sabendo que podera mexer no autor, titulo e data de lancamento")
    print ("0 - Sair ")
    print ("1 - Adicionar ")
    print ("2 - Atualizar ")
    print ("3 - Deletar ")
    print ("4 - Visualizar tabela ")

    escolha = input("digite aqui: ")
    
    #validacao da escolha
    if not escolha in opcao:  
        print("Opção inválida")
        continue

    #escolha 
    match escolha:
        case "0":
            print ("Voce saiu")
            break
       
        case "1":
            while True:         #usei para fazer uma repetiçao para a validaçao

                titulo = input("Qual o Título do seu livro? ")
                autor = input(f"Qual o autor do livro {titulo}? ")
                print("Em qual data o seu livro foi lançado? ")
                ano_de_lancamento = input("Escreva aqui (ano-mes-dia): ")
                
                try:
                    criar_livros (titulo, autor, ano_de_lancamento)
                    #mensagem
                    print ("=================")     
                    print("Ok tudo certo, adicionamos as informações sobre seu livro com sucesso.")
                    print ("=================")     
                    # Read
                        
                    ler_livros()
                    print ("=================")   

                    break   
                except:
                    print ("Ocorreu um erro, tente novamente")
                    continue

                #Caso queira fazer denovo ou sair
            while True:
                continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
                if continuar == "1":
                    break
                elif continuar == "2":
                    print("Muito obrigado por utilizar nossa biblioteca.")
                    exit()
                else:
                    print("Valor inválido por favor responda com 1 ou 2.")



        
        case "2":

            while True:
                print ("Selecione o id do item que voce queira atualizar")
                ler_livros()
                idd = input("Escreva aqui: ")
                novo_x = input ("O que você gostaria de atualizar \n1 - Título \n2 - Autor \n3 - data de lançamento \nEscreva aqui: ")
                
                #validacao
                if not novo_x in opcao[:4]:
                    print ("Selecione uma das alternativas")
                    continue
                
                if novo_x == "1":
                    novo_x = "titulo"
                elif novo_x == "2":
                    novo_x = "autor"
                elif novo_x == "3":
                    novo_x = "ano_de_lancamento"

                novo_y = input(f"Qual o seu novo {novo_x}: ")



                atualizar_livros(idd, novo_x)

                #finalizacao da cadeia while true
                break 

            #mensagem
            print ("=================")     
            print ("Ok tudo certo, adicionamos as informações sobre seu livro com sucesso.")
            print ("=================")     
        
            # Read
            
            ler_livros()
            print ("=================")     

             #Caso queira fazer denovo ou sair
            while True:
                continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
                if continuar == "1":
                    break
                elif continuar == "2":
                    print("Muito obrigado por utilizar nossa biblioteca.")
                    exit()
                else:
                    print("Valor inválido por favor responda com 1 ou 2.")

        case "3":
            ler_livros()
            print ("Qual livro você gostaria de excluir?")
            id_livros = input ("Digite aqui: ")
            deletar_livros(id_livros)
            ler_livros()
          
            #mensagem
            
            print ("=================")
            print ("Livro deletado com sucesso!!")
            print ("=================")

             #Caso queira fazer denovo ou sair
            while True:
                continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
                if continuar == "1":
                    break
                elif continuar == "2":
                    print("Muito obrigado por utilizar nossa biblioteca.")
                    exit()
                else:
                    print("Valor inválido por favor responda com 1 ou 2.")

        case "4":
            while True:
                print ("=================")     
                ler_livros()
                print ("=================")     
                break

                #Caso queira fazer denovo ou sair
            while True:
                continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
                if continuar == "1":
                    break
                elif continuar == "2":
                    print("Muito obrigado por utilizar nossa biblioteca.")
                    exit()
                else:
                    print("Valor inválido por favor responda com 1 ou 2.")
