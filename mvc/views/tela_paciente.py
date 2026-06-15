import PySimpleGUI as sg

class TelaPaciente:
    def __init__(self):
        self.window = None

    def init_components(self, p=None):
        sg.theme('LightBlue')
        nome = p.nome if p else ""
        nascimento = p.nascimento.strftime('%d/%m/%Y') if p else ""
        altura = p.altura if p else ""
        peso = p.peso if p else ""
        genero = p.genero if p else ""

        layout = [
            [sg.Text('Cadastro de Paciente', font=('Helvetica', 16), justification='center', expand_x=True)],
            [sg.Text('Nome:', size=(20, 1)), sg.InputText(nome, key='nome')],
            [sg.Text('Data de Nasc. (DD/MM/AAAA):', size=(20, 1)), sg.InputText(nascimento, key='data')],
            [sg.Text('Altura (m):', size=(20, 1)), sg.InputText(altura, key='altura')],
            [sg.Text('Peso (kg):', size=(20, 1)), sg.InputText(peso, key='peso')],
            [sg.Text('Gênero (M/F):', size=(20, 1)), sg.InputText(genero, key='genero')],
            [sg.Button('Salvar', size=(10, 1)), sg.Button('Cancelar', size=(10, 1))]
        ]
        self.window = sg.Window('Paciente', layout)

    def abrir(self, p=None):
        self.init_components(p)
        
    def ler_eventos(self):
        if self.window:
            return self.window.read()
        return None, None

    def fechar(self):
        if self.window:
            self.window.close()
            self.window = None
