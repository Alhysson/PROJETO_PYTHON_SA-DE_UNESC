import PySimpleGUI as sg

class TelaListagem:
    def mostrar_lista(self, lista):
        if not lista:
            sg.popup("A lista está vazia.", title="Aviso")
            return False

        dados = [[p.id, p.nome, p.altura, p.peso] for p in lista]
        cabecalhos = ['ID', 'Nome', 'Altura', 'Peso']

        layout = [
            [sg.Table(values=dados, headings=cabecalhos, max_col_width=25,
                      auto_size_columns=True, justification='right',
                      num_rows=min(len(dados), 15), key='-TABLE-')],
            [sg.Button('Voltar', size=(10, 1))]
        ]
        window = sg.Window('Lista de Pacientes', layout, element_justification='c')
        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, 'Voltar'):
                break
        window.close()
        return True

    def mostrar_detalhes(self, p):
        import PySimpleGUI as sg
        from mvc.controllers.gerar_pdf import gerar_pdf_paciente

        genero_ext = "Masculino" if p.genero == "M" else "Feminino"
        imc = p.calcular_imc()
        tmb = p.calcular_tmb()

        # Classificação do IMC
        if imc < 18.5:
            classif = "Abaixo do peso"
        elif imc < 25.0:
            classif = "Peso normal ✓"
        elif imc < 30.0:
            classif = "Sobrepeso"
        elif imc < 35.0:
            classif = "Obesidade Grau I"
        elif imc < 40.0:
            classif = "Obesidade Grau II"
        else:
            classif = "Obesidade Grau III"

        texto = (
            f"ID: {p.id}\n"
            f"Nome: {p.nome}\n"
            f"Nascimento: {p.nascimento.strftime('%d/%m/%Y')}\n"
            f"Gênero: {genero_ext}\n"
            f"Altura: {p.altura} m\n"
            f"Peso: {p.peso} kg\n"
            f"Idade: {p.calcular_idade()} anos\n"
            f"IMC: {imc:.2f}  ({classif})\n"
            f"TMB: {tmb:.2f} kcal/dia\n"
        )

        layout = [
            [sg.Multiline(texto, size=(45, 12), disabled=True,
                          font=('Helvetica', 11), background_color='#eaf4fc',
                          no_scrollbar=False, key='-DETALHES-')],
            [sg.Button('🖨️  Imprimir (PDF)', size=(20, 1), font=('Helvetica', 11)),
             sg.Button('OK', size=(10, 1), font=('Helvetica', 11))]
        ]

        window = sg.Window(f'Detalhes: {p.nome}', layout,
                           element_justification='c', modal=True, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, 'OK'):
                break
            if event == '🖨️  Imprimir (PDF)':
                caminho = sg.popup_get_file(
                    'Salvar PDF como:',
                    title='Salvar Relatório',
                    save_as=True,
                    default_extension='.pdf',
                    file_types=(('PDF Files', '*.pdf'),),
                    default_path=f'relatorio_{p.nome.split()[0].lower()}.pdf'
                )
                if caminho:
                    try:
                        gerar_pdf_paciente(p, caminho)
                        sg.popup(f'PDF salvo com sucesso!\n{caminho}',
                                 title='Sucesso', font=('Helvetica', 11))
                    except Exception as e:
                        sg.popup_error(f'Erro ao gerar PDF:\n{e}',
                                       title='Erro', font=('Helvetica', 11))

        window.close()
