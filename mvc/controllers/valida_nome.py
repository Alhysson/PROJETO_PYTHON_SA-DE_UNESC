def parse_nome(v):
    v = v.strip()
    if not v:
        raise ValueError("Nome obrigatorio")
    return v
