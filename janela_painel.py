from conexao import *
from tabela_user import *

def Janela_Painel():
    consultar()
    sg.theme('PythonPlus')
    layout = [
        [sg.Text('Insira um Produto')],
        [sg.Text('Nome do produto'), sg.Input(key='usuario')],
        [sg.Text('Valor do Produto'), sg.Input(key='senha')],
        [sg.Text('Quantidade'), sg.Input(key='qtd')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')],
        [sg.Button('Primeira View', key='view1'), sg.Button('Segunda View', key='view2'), sg.Input('', key='nameproduto'), sg.Button('Mostrar', key='botaomostrar')],
        [sg.Text('', key="view")]

    ]
    return sg.Window('Tela de Cadastro', layout=layout, finalize=True)
  
