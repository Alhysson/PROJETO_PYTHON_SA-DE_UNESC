def parse_genero(v):
    g = v.strip().upper()
    if g not in ["M", "F"]:
        raise ValueError("M ou F")
    return g
