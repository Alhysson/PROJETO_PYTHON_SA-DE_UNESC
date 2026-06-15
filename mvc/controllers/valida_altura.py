def parse_altura(v):
    try:
        n = float(v.replace(",", "."))
    except ValueError:
        raise ValueError("Altura invalida: use numeros (ex: 1.75)")

    if n < 0.64 or n > 2.51:
        raise ValueError("Altura invalida: deve ser entre 0.64 m e 2.51 m")

    return n
