from conexao import *
from main import *

def Janela_Cadastro():
    consultar()
    sg.theme('PythonPlus')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='usuario')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
    ]


    return sg.Window('Tela de Cadastro', layout=layout, finalize=True)
  


