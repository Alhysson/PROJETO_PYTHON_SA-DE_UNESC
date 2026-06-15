def parse_peso(v):
    try:
        n = float(v.replace(",", "."))
    except ValueError:
        raise ValueError("Peso invalido: use numeros (ex: 70.5)")

    if n < 20 or n > 500:
        raise ValueError("Peso invalido: deve ser entre 20 kg e 500 kg")

    return n
