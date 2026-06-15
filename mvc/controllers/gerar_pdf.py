import os
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable


def gerar_pdf_paciente(paciente, caminho_arquivo):
    """Gera um PDF com os dados nutricionais do paciente."""

    doc = SimpleDocTemplate(
        caminho_arquivo,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()

    # Estilos personalizados
    titulo_style = ParagraphStyle(
        'Titulo',
        parent=styles['Title'],
        fontSize=20,
        textColor=colors.HexColor('#1a5276'),
        spaceAfter=6,
    )
    subtitulo_style = ParagraphStyle(
        'Subtitulo',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#5d6d7e'),
        spaceAfter=16,
    )
    secao_style = ParagraphStyle(
        'Secao',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#1a5276'),
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=6,
    )
    rodape_style = ParagraphStyle(
        'Rodape',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=1,  # centralizado
    )

    genero_ext = "Masculino" if paciente.genero == "M" else "Feminino"
    imc = paciente.calcular_imc()
    tmb = paciente.calcular_tmb()
    idade = paciente.calcular_idade()

    # Classificação do IMC
    if imc < 18.5:
        classif_imc = "Abaixo do peso"
        cor_imc = colors.HexColor('#e67e22')
    elif imc < 25.0:
        classif_imc = "Peso normal"
        cor_imc = colors.HexColor('#27ae60')
    elif imc < 30.0:
        classif_imc = "Sobrepeso"
        cor_imc = colors.HexColor('#e67e22')
    elif imc < 35.0:
        classif_imc = "Obesidade Grau I"
        cor_imc = colors.HexColor('#e74c3c')
    elif imc < 40.0:
        classif_imc = "Obesidade Grau II"
        cor_imc = colors.HexColor('#c0392b')
    else:
        classif_imc = "Obesidade Grau III"
        cor_imc = colors.HexColor('#922b21')

    conteudo = []

    # Cabeçalho
    conteudo.append(Paragraph("Relatório Nutricional", titulo_style))
    conteudo.append(Paragraph(
        f"Gerado em: {datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')}",
        subtitulo_style
    ))
    conteudo.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a5276')))
    conteudo.append(Spacer(1, 0.4 * cm))

    # Dados pessoais
    conteudo.append(Paragraph("📋 Dados Pessoais", secao_style))
    dados_pessoais = [
        ['Campo', 'Informação'],
        ['ID', str(paciente.id)],
        ['Nome', paciente.nome],
        ['Data de Nascimento', paciente.nascimento.strftime('%d/%m/%Y')],
        ['Idade', f'{idade} anos'],
        ['Gênero', genero_ext],
    ]
    tabela_pessoal = Table(dados_pessoais, colWidths=[5 * cm, 11 * cm])
    tabela_pessoal.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5276')),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#eaf4fc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#eaf4fc')]),
        ('FONTNAME',   (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE',   (0, 1), (-1, -1), 10),
        ('GRID',       (0, 0), (-1, -1), 0.5, colors.HexColor('#aed6f1')),
        ('ALIGN',      (0, 0), (-1, -1), 'LEFT'),
        ('PADDING',    (0, 0), (-1, -1), 6),
    ]))
    conteudo.append(tabela_pessoal)
    conteudo.append(Spacer(1, 0.4 * cm))

    # Dados antropométricos
    conteudo.append(Paragraph("📊 Dados Antropométricos", secao_style))
    dados_antro = [
        ['Indicador', 'Valor', 'Classificação / Observação'],
        ['Altura', f'{paciente.altura:.2f} m', '—'],
        ['Peso', f'{paciente.peso:.1f} kg', '—'],
        ['IMC', f'{imc:.2f} kg/m²', classif_imc],
        ['TMB (Mifflin-St Jeor)', f'{tmb:.2f} kcal/dia', 'Calorias em repouso'],
    ]
    tabela_antro = Table(dados_antro, colWidths=[5 * cm, 4 * cm, 7 * cm])
    tabela_antro.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5276')),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 11),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#eaf4fc')]),
        ('FONTNAME',   (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE',   (0, 1), (-1, -1), 10),
        ('GRID',       (0, 0), (-1, -1), 0.5, colors.HexColor('#aed6f1')),
        ('ALIGN',      (0, 0), (-1, -1), 'LEFT'),
        ('PADDING',    (0, 0), (-1, -1), 6),
        # Coluna IMC com cor de classificação
        ('TEXTCOLOR',  (2, 3), (2, 3), cor_imc),
        ('FONTNAME',   (2, 3), (2, 3), 'Helvetica-Bold'),
    ]))
    conteudo.append(tabela_antro)
    conteudo.append(Spacer(1, 0.6 * cm))

    # Rodapé
    conteudo.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#aed6f1')))
    conteudo.append(Spacer(1, 0.2 * cm))
    conteudo.append(Paragraph(
        "Documento gerado automaticamente pelo Nutrição App — MVC",
        rodape_style
    ))

    doc.build(conteudo)
    return caminho_arquivo
