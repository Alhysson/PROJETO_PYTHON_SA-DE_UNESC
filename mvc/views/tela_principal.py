import PySimpleGUI as sg

class TelaPrincipal:
    def __init__(self):
        self.window = None

    def init_components(self):
        sg.theme('LightBlue')
        layout = [
            [sg.Text('Menu Nutrição App', font=('Helvetica', 26, 'bold'), justification='center', expand_x=True, pad=(0, 20))],
            [sg.Button('Cadastrar', size=(20, 3), font=('Helvetica', 12)),
             sg.Button('Listar',    size=(20, 3), font=('Helvetica', 12)),
             sg.Button('Excluir',   size=(20, 3), font=('Helvetica', 12))],
            [sg.Button('Detalhes',  size=(20, 3), font=('Helvetica', 12)),
             sg.Button('Atualizar', size=(20, 3), font=('Helvetica', 12)),
             sg.Button('Sair',      size=(20, 3), font=('Helvetica', 12))]
        ]
        self.window = sg.Window('Nutrição - MVC', layout, element_justification='c', size=(780, 280), margins=(20, 20))

    def ler_eventos(self):
        if self.window is None:
            self.init_components()
        return self.window.read()

    def fechar(self):
        if self.window:
            self.window.close()
            self.window = None
