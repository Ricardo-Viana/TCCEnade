MAPEAMENTO = {
    "CO_CATEGAD": {
        1: "Pública Federal",
        2: "Pública Estadual",
        3: "Pública Municipal",
        4: "Privada CFL",
        5: "Privada SFL",
        7: "Especial"
    },
    "CO_ORGACAD": {
        10019: "CFET",
        10020: "C. Universitário",
        10022: "Faculdade",
        10026: "IFECT",
        10028: "Universidade"
    },
    "CO_MODALIDADE": {
        0: "EaD",
        1: "Presencial"
    },
    "CO_REGIAO_CURSO": {
        1: "Norte",
        2: "Nordeste",
        3: "Sudeste",
        4: "Sul",
        5: "Centro-Oeste"
    }
}

def mapeamento_valores(tabela):
    for coluna, mapeamento in MAPEAMENTO.items():
        if coluna in tabela.columns:
            tabela[coluna] = tabela[coluna].replace(mapeamento)
    return tabela