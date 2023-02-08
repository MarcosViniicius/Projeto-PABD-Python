from conexao import criar_conexao, fechar_conexao
from PySimpleGUI import PySimpleGUI as sg
import datetime

hora_atual = datetime.datetime.now()

con = criar_conexao("localhost", "3306", "root", "", "project")

def insere_produto(con, nameProduct, price, QTD, userId, updatedAt, createdAt):
    cursor = con.cursor()
    sql = "INSERT INTO product (nameProduct, price, QTD, userId, updatedAt, createdAt) values (%s, %s, %s, %s, %s, %s)"
    valores = (nameProduct, price, QTD, userId, updatedAt, createdAt)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def select_todos_produtos(con):
    cursor = con.cursor()
    sql = "SELECT id, nameProduct FROM product"
    cursor.execute(sql)

    for (id, nameProduct) in cursor:
        print(id, nameProduct)
    
    cursor.close()

def main():
    con = criar_conexao("localhost", "3306", "root", "", "project")


    insere_produto(con, "Teste", "123", hora_atual, hora_atual)
    select_todos_produtos(con)

    fechar_conexao(con)

def select_produto(con):
    cursor = con.cursor()
    sql = "SELECT id FROM Users WHERE name = lucas"
    cursor.execute(sql)

    for (id, name) in cursor:
        print(id, name)
    
    cursor.close()

if __name__ == "__tabela_products__":
    main()
