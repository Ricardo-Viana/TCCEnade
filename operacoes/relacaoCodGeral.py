import pandas as pd

def relacionarTabelasCodGeral(tabela_relacionada, ano):
    cine_rotulo = pd.read_csv('cinerotuloenade.csv')
    
    tabela_combinada = pd.merge(
        tabela_relacionada,
        cine_rotulo[[f'cod_enade_{ano}', 'cod_geral']].rename(columns={'cod_geral': f'cod_geral_{ano}'}),
        left_on='CO_GRUPO',
        right_on=f'cod_enade_{ano}',
        how='left'
    )

    return tabela_combinada