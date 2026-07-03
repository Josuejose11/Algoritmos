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

#def erro
def erro():
    print (f"------------")
    print (f"*Ocorreu um erro, tente novamente*")
    print (f"------------")

#validacao de id
def senha_(id_, senha):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM clientes WHERE id = %s AND senha = %s"
    valores = (id_, senha)
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
    







denovo()