import pandas as pd

def relacionarTabelasCodGeral(tabela_relacionada, ano_grupo):
    cine_rotulo = pd.read_csv('cinerotuloenade.csv')
    
    tabela_combinada = pd.merge(
        tabela_relacionada,
        cine_rotulo[[f'cod_enade_{ano_grupo}', 'cod_geral']].rename(columns={'cod_geral': f'cod_geral_{ano_grupo}'}),
        left_on='CO_GRUPO',
        right_on=f'cod_enade_{ano_grupo}',
        how='left'
    )

    return tabela_combinada