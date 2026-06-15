from mvc.views.tela_principal import TelaPrincipal
from mvc.views.tela_listagem import TelaListagem
from mvc.controllers import acoes
from mvc.models.paciente_dao import PacienteDAO
import PySimpleGUI as sg

class NutricaoController:
    def __init__(self):
        self.dao = PacienteDAO()
        self.tela = TelaPrincipal()

    def rodar(self):
        self.tela.init_components()
        while True:
            event, values = self.tela.ler_eventos()
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif event == 'Cadastrar':
                acoes.cadastrar(self.dao)
            elif event == 'Listar':
                tela_lista = TelaListagem()
                tela_lista.mostrar_lista(self.dao.listar())
            elif event == 'Excluir':
                acoes.excluir(self.dao)
            elif event == 'Detalhes':
                acoes.ver(self.dao)
            elif event == 'Atualizar':
                acoes.atualizar(self.dao)
        self.tela.fechar()
