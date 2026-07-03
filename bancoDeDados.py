# pip install mysql-connector-python         - codigo para integrar o sql e o python

alunos = []

def create(nome, idade):
    alunos.append ({'nome': nome, 'idade':idade})

def read():
    for aluno in alunos:
        print (aluno)

def update(indice, nome, idade):
    alunos[indice]['nome'] = nome
    alunos[indice]['idade'] = idade

def delete(indice):
    alunos.pop(indice)

print ("-----CREATE-----")

create ("ana", 20)
create ("bruno", 22)
read()

print ("-----UPDATE-----")

update(0, "ana clara", 21)
read()

print ("-----DELETE-----")

delete (0)
read() 