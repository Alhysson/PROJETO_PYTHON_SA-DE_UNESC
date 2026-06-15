import PySimpleGUI as sg
from mvc.models import paciente
from mvc.views import saidas
from mvc.views.tela_paciente import TelaPaciente
from mvc.views.tela_listagem import TelaListagem
from mvc.controllers import valida_nome, valida_data, valida_altura, valida_peso, valida_genero

def cadastrar(dao):
    tela = TelaPaciente()
    tela.abrir()
    while True:
        botao, valores = tela.ler_eventos()
        if botao in (None, 'Cancelar', sg.WIN_CLOSED):
            break
        if botao == 'Salvar':
            try:
                n = valida_nome.parse_nome(valores['nome'])
                d = valida_data.parse_data(valores['data'])
                a = valida_altura.parse_altura(valores['altura'])
                p = valida_peso.parse_peso(valores['peso'])
                g = valida_genero.parse_genero(valores['genero'])
                novo = paciente.Paciente(n, d, a, p, g)
                dao.inserir(novo)
                saidas.mostrar_msg("Cadastrado com sucesso!")
                break
            except ValueError as e:
                saidas.mostrar_erro(str(e))
    tela.fechar()

def excluir(dao):
    lista = dao.listar()
    if not lista:
        saidas.mostrar_erro("A lista está vazia.")
        return
        
    idx_str = sg.popup_get_text("ID do paciente para excluir:", title="Excluir")
    if idx_str:
        try:
            idx = int(idx_str)
            if dao.excluir(idx):
                saidas.mostrar_msg("Removido com sucesso!")
            else:
                saidas.mostrar_erro("Paciente não encontrado")
        except ValueError:
            saidas.mostrar_erro("ID inválido!")

def ver(dao):
    lista = dao.listar()
    if not lista:
        saidas.mostrar_erro("A lista está vazia.")
        return
        
    idx_str = sg.popup_get_text("ID do paciente para ver detalhes:", title="Detalhes")
    if idx_str:
        try:
            idx = int(idx_str)
            p = dao.buscar_por_id(idx)
            if p:
                tela = TelaListagem()
                tela.mostrar_detalhes(p)
            else:
                saidas.mostrar_erro("Paciente não encontrado")
        except ValueError:
            saidas.mostrar_erro("ID inválido!")

def atualizar(dao):
    lista = dao.listar()
    if not lista:
        saidas.mostrar_erro("A lista está vazia.")
        return
        
    idx_str = sg.popup_get_text("ID do paciente para atualizar:", title="Atualizar")
    if idx_str:
        try:
            idx = int(idx_str)
            p = dao.buscar_por_id(idx)
            if not p:
                saidas.mostrar_erro("Paciente não encontrado")
                return
                
            tela = TelaPaciente()
            tela.abrir(p)
            while True:
                botao, valores = tela.ler_eventos()
                if botao in (None, 'Cancelar', sg.WIN_CLOSED):
                    break
                if botao == 'Salvar':
                    try:
                        n = valida_nome.parse_nome(valores['nome'])
                        d = valida_data.parse_data(valores['data'])
                        a = valida_altura.parse_altura(valores['altura'])
                        pe = valida_peso.parse_peso(valores['peso'])
                        g = valida_genero.parse_genero(valores['genero'])
                        novo_p = paciente.Paciente(n, d, a, pe, g)
                        dao.atualizar(idx, novo_p)
                        saidas.mostrar_msg("Atualizado com sucesso!")
                        break
                    except ValueError as e:
                        saidas.mostrar_erro(str(e))
            tela.fechar()
        except ValueError:
            saidas.mostrar_erro("ID inválido!")
