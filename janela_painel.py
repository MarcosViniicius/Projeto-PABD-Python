from conexao import *
from main import *

def Janela_Painel():
    consultar()
    sg.theme('PythonPlus')
    layout = [
        [sg.Text('Nome do produto'), sg.Input(key='nome_produto')],
        [sg.Text('Valor do produto'), sg.Input(key='valor_produto')],
        [sg.Button('Adicionar')]
    ]


    return sg.Window('Painel de controle', layout=layout, finalize=True)



