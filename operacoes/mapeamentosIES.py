MAPEAMENTO = {
    "CO_CATEGAD": {
        1: "Pública Federal",
        2: "Pública Estadual",
        3: "Pública Municipal",
        4: "Privada com fins lucrativos",
        5: "Privada sem fins lucrativos",
        7: "Especial"
    },
    "CO_ORGACAD": {
        10019: "Centro Federal de Educação Tecnológica",
        10020: "Centro Universitário",
        10022: "Faculdade",
        10026: "Instituto Federal de Educação, Ciência e Tecnologia",
        10028: "Universidade"
    },
    "CO_MODALIDADE": {
        0: "EaD",
        1: "Presencial"
    },
    "CO_REGIAO_CURSO": {
        1: "Região Norte",
        2: "Região Nordeste",
        3: "Região Sudeste",
        4: "Região Sul",
        5: "Região Centro-Oeste"
    }
}

def mapeamento_valores(tabela):
    for coluna, mapeamento in MAPEAMENTO.items():
        if coluna in tabela.columns:
            tabela[coluna] = tabela[coluna].replace(mapeamento)
    return tabela