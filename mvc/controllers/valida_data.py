import datetime

def parse_data(v):
    try:
        d = datetime.datetime.strptime(v, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("Data invalida (use DD/MM/AAAA)")

    if d > datetime.date.today():
        raise ValueError("Data de nascimento não pode ser futura")

    hoje = datetime.date.today()
    idade = hoje.year - d.year - ((hoje.month, hoje.day) < (d.month, d.day))

    if idade < 18:
        raise ValueError("Paciente deve ter pelo menos 18 anos")
    if idade > 115:
        raise ValueError("Idade maxima permitida: 115 anos")

    return d
