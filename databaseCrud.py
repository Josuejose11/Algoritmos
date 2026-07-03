# CRUD - Python e SQL


import mysql.connector
from mysql.connector import Error


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database ='crud_python'
        )
        return conexao
    except Error as e:
        print (f"Erro ao conectar ao mySql: {e}")
        return None
    
# CREATE / CRIAR

def criar_usuario(nome,email):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)

    cursor.execute(sql, valores)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) inserido(s).")
    cursor.close()
    conn.close()

criar_usuario ('josue', 'josuejose11@outlook.com')


# READ / LER

def ler_usuarios():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM usuarios")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")

    cursor.close()
    conn.close()

ler_usuarios()


# UPDATE / ATUALIZAR 

def atualizar_email(id_usuario, novo_email):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = ("UPDATE usuarios SET email = %s WHERE id = %s")
    valores = (novo_email, id_usuario)

    cursor.execute(sql, valores)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) atualizado(s).")
    cursor.close()
    conn.close()


# DELETAR 

def deletar_usuario(id_usuario): 
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = ("DELETE FROM usuarios WHERE id = %s")
    valor = (id_usuario)

    cursor.execute(sql, valor)
    conn.commit()

    print (f"{cursor.rowcount} registro(s) apagado(s).")
    cursor.close()
    conn.close()

