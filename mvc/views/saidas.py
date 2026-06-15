import PySimpleGUI as sg

def mostrar_erro(msg):
    sg.popup_error(f"Erro: {msg}", title="Erro")

def mostrar_msg(msg):
    sg.popup(f"Sucesso: {msg}", title="Sucesso")
