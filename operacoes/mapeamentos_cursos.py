MAPEAMENTO = {
    "CO_GRUPO": {
        72: "Tec. ADS",
        4006: "SI",
        4004: "BCC",
        79: "Tec. Redes",
        6409: "Tec. Gestão da TI"
    }
}

def mapeamento_valores(tabela):
    for coluna, mapeamento in MAPEAMENTO.items():
        if coluna in tabela.columns:
            tabela[coluna] = tabela[coluna].replace(mapeamento)
    return tabela