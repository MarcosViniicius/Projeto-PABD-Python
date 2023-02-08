from PySimpleGUI import PySimpleGUI as sg
from conexao import *
from janela_painel import *
from janela_cadastro import *
from tabela_user import *
from tabela_products import *
import re

def Janela_Login():
    consultar()
    sg.theme('PythonPlus')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
        [sg.Text('Não tem um Login?'), sg.Button('Cadastre-se')],
        [sg.Button('Entrar'), sg.Button('Cancelar')],
        [sg.Text('', key="msg_senha")],
    ]   
    print(usuariosdb)
    print(senhasdb)
    return sg.Window('Tela de login', layout=layout, finalize=True)

con = criar_conexao("localhost", "3306", "root", "", "project")
cursor = con.cursor()

Janela1, Janela2, Janela3 = Janela_Login(), None, None
janela1 = Janela_Login

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 or event == sg.WIN_CLOSED or event=="Cancelar":
        break

    if values['usuario'] in usuariosdb and values['senha'] in senhasdb and window == Janela1 and event == 'Entrar':
        usuario_logado = [] 
        id_usuario_logado = []
        usuario_logado.append(values['usuario'])
        resid = str(usuario_logado)[1:-1]
        cursor = con.cursor()
        sql = f"SELECT id FROM users where name = {resid}"
        cursor.execute(sql)
        for id_user in cursor:
            id_usuario_logado.append(id_user) 
        res2 = str(id_usuario_logado)[1:-1]
        id_usuario = re.sub("[(),]","", res2)
        print(id_usuario)
        id_usuario_logado.clear()
        Janela2 = Janela_Painel()
        Janela1.hide() 
        
    if values['usuario'] != usuariosdb and values['senha'] != usuariosdb:  
        Janela1["msg_senha"].update('Senha ou usuário incorreto.')

    if event == 'Cadastre-se':
        print('Tela cadastro')
        conectar()
        Janela3 = Janela_Cadastro()
        Janela1.hide() 

    if window == Janela3 and event == 'Voltar':
        conectar()
        Janela3.hide()
        Janela1.un_hide()

    if window == Janela3 and event == 'Cadastrar':
        if values['usuario']:
            print(values['usuario'])
            insere_usuario(con, values['usuario'], values['senha'], hora_atual, hora_atual)


    if window == Janela2 and event == 'Cadastrar':
        insere_produto(con, values['usuario'], values['senha'], values['qtd'], id_usuario, hora_atual, hora_atual)

    if window == Janela2 and event == 'view1':
        res = []
        con = criar_conexao("localhost", "3306", "root", "", "project")
        cursor = con.cursor()
        sql = "SELECT * FROM vwVisao01"
        cursor.execute(sql)
        for resul in cursor:
            res.append(resul)
            res.append('|')
        res2 = str(res)[1:-1]
        resfinal= re.sub("[(),]","", res2)
        Janela2["view"].update(resfinal)
    
    if window == Janela2 and event == 'view2':
        res = []
        resids = str(id_usuario_logado)[1:-1]
        print(resids)
        con = criar_conexao("localhost", "3306", "root", "", "project")
        cursor = con.cursor()
        sql = f"SELECT * FROM vwVisao02 WHERE id = {id_usuario_logado}"
        cursor.execute(sql)
        for resul in cursor:
            res.append(resul)
            res.append('|')
        res2 = str(res)[1:-1]
        resfinal= re.sub("[(),]","", res2)
        Janela2["view"].update(resfinal)
        print(resfinal)

    if window == Janela2 and event == 'botaomostrar':
        Janela2["view"].update('Produto disponível')




