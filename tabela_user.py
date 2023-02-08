from conexao import criar_conexao, fechar_conexao
from PySimpleGUI import PySimpleGUI as sg


import datetime

hora_atual = datetime.datetime.now()

con = criar_conexao("localhost", "3306", "root", "", "project")

def insere_usuario(con, name, password, updatedAt, createdAt):
    cursor = con.cursor()
    sql = "INSERT INTO Users (name, password, updatedAt, createdAt) values (%s, %s, %s, %s)"
    valores = (name, password, updatedAt, createdAt)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def select_todos_usuarios(con):
    cursor = con.cursor()
    sql = "SELECT id, name FROM Users"
    cursor.execute(sql)

    for (id, name) in cursor:
        print(id, name)
    
    cursor.close()


def main():
    con = criar_conexao("localhost", "3306", "root", "", "project")

    insere_usuario(con, "Teste", "123", hora_atual, hora_atual)
    select_todos_usuarios(con)

    fechar_conexao(con)

def conectar():
    con = criar_conexao("localhost", "3306", "root", "", "project")


senhasdb = []
usuariosdb = []

def consultar():
    usuariosdb.clear()
    senhasdb.clear()
    consulta_sql = "select * from Users"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    infos = cursor.fetchall()
    for info in infos:
        usuariosdb.append(info[1])
        senhasdb.append(info[2])
    cursor.close()
    # print(senhasdb)
    # print(usuariosdb)
    # print(cursor.rowcount)

if __name__ == "__tabela_user__":
    main()

    