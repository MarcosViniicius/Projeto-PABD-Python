import mysql.connector
from PySimpleGUI import PySimpleGUI as sg


def criar_conexao(host, port, usuario, senha, banco):
    return mysql.connector.connect(host=host, port=port,  user=usuario, password=senha, database=banco)


def fechar_conexao(con):
    return con.close()

