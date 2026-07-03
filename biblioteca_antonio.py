import mysql.connector
 
# -----------------------------
# CONEXÃO
# -----------------------------
 
try:
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="biblioteca_db"
    )
    cursor = conexao.cursor()
except Exception as e:
    print("Erro ao conectar ao banco:", e)
    exit()
 
 
# -----------------------------
# FUNÇÕES
# -----------------------------
 
def cadastrar_autor():
    try:
        nome = input("Nome do autor: ")
        nacionalidade = input("Nacionalidade: ")
 
        sql = "INSERT INTO autores (nome, nacionalidade) VALUES (%s, %s)"
        cursor.execute(sql, (nome, nacionalidade))
        conexao.commit()
 
        print("Autor cadastrado com sucesso!")
 
    except Exception as e:
        print("Erro ao cadastrar autor:", e)
 
 
def listar_autores():
    try:
        cursor.execute("SELECT * FROM autores")
        autores = cursor.fetchall()
 
        print("\nAUTORES:")
        for autor in autores:
            print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")
 
    except Exception as e:
        print("Erro ao listar autores:", e)
 
 
def cadastrar_livro():
    try:
        listar_autores()
 
        fk_id_autor = int(input("\nDigite o ID do autor: "))
 
        cursor.execute("SELECT * FROM autores WHERE id_autor = %s", (fk_id_autor,))
        autor = cursor.fetchone()
 
        if autor is None:
            print("Autor não encontrado!")
            return
 
        titulo = input("Título do livro: ")
        ano = int(input("Ano de publicação: "))
 
        sql = """
        INSERT INTO livros (titulo, ano_publicacao, fk_id_autor)
        VALUES (%s, %s, %s)
        """
 
        cursor.execute(sql, (titulo, ano, fk_id_autor))
        conexao.commit()
 
        print("Livro cadastrado com sucesso!")
 
    except ValueError:
        print("Entrada inválida!")
    except Exception as e:
        print("Erro ao cadastrar livro:", e)
 
 
def listar_livros():
    try:
        sql = """
        SELECT livros.id_livro, livros.titulo, livros.ano_publicacao, autores.nome
        FROM livros
        INNER JOIN autores ON livros.fk_id_autor = autores.id_autor
        """
 
        cursor.execute(sql)
        livros = cursor.fetchall()
 
        print("\nACERVO:")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[2]} | Autor: {livro[3]}")
 
    except Exception as e:
        print("Erro ao listar livros:", e)
 
 
def reset_total():
    confirmacao = input("Tem certeza que deseja apagar TODOS os dados? (s/n): ")
 
    if confirmacao.lower() == 's':
        try:
            cursor.execute("DELETE FROM autores")
            conexao.commit()
            print("Banco resetado com sucesso!")
 
        except Exception as e:
            print("Erro ao resetar:", e)
 
 
# -----------------------------
# MENU
# -----------------------------
 
def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar Autor")
        print("2 - Cadastrar Livro")
        print("3 - Listar Livros")
        print("4 - Listar Autores")
        print("5 - Reset Total")
        print("0 - Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cadastrar_autor()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            listar_autores()
        elif opcao == "5":
            reset_total()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
 
 
# -----------------------------
# EXECUÇÃO
# -----------------------------
 
menu()
 
cursor.close()
conexao.close()