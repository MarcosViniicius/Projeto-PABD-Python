from PySimpleGUI import PySimpleGUI as sg
from conexao import *
from janela_painel import *
from janela_cadastro import *
from main import *



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


    return sg.Window('Tela de login', layout=layout, finalize=True)


Janela1, Janela2, janela3 = Janela_Login(), None, None
janela1 = Janela_Login

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 or event == sg.WIN_CLOSED or event=="Cancelar":
        break

    if values['usuario'] in usuariosdb and values['senha'] in senhasdb and window == Janela1 and event == 'Entrar':
        # main()
        print('Bem-vindo')
        janela2 = Janela_Painel()
        Janela1.hide() 
        
    if values['usuario'] != usuariosdb and values['senha'] != usuariosdb:  
        Janela1["msg_senha"].update('Senha ou usuário incorreto.')

    if event == 'Cadastre-se':
        print('Tela cadastro')
        conectar()
        janela3 = Janela_Cadastro()
        Janela1.hide() 

    if window == janela3 and event == 'Voltar':
        consultar()
        janela3.hide()
        Janela1.un_hide()

    if window == janela3 and event == 'Cadastrar':
        if values['usuario']:
            print(values['usuario'])
            insere_usuario(con, values['usuario'], values['senha'], hora_atual, hora_atual)









# 
# while True:
#     window,event,values = sg.read_all_windows()
#     if window == Janela1 and event == sg.WIN_CLOSED:
#         break

#     if window == Janela1 and event == 'Entrar':
#         Janela2 = Janela_Painel()
#         Janela1.hide()

if __name__ == "__main__":
    Janela_Login()

# interface


# while True:
#     eventos, valores = janela.read_all_windows()
#     if eventos == sg.WIN_CLOSED:
#         break
#     if valores['usuario'] == 'teste' and valores['senha'] == '123':
#         # main()
#         print('Bem-vindo')
#         Janela_Painel()
#         Janela1.hide()
