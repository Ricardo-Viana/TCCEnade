# Análise dos Microdados do Enade

Esse projeto tem como objetivo automatizar cálculos estatísticos sobre o ENADE com o intuito de embasar possíveis pesquisas.

## Índice
- [Instalação](#instalação)
- [Uso](#uso)
- [Arquivos](#arquivos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Autores](#autores)

## Instalação
```bash
# Clone o repositório
git clone https://github.com/Ricardo-Viana/TCCEnade

# Entre no diretório
cd TCCENADE

# Instale as dependências
pip install -r requirements.txt
```

## Uso

```bash
# Executar o código
python main.py [ARGUMENTOS]

#Argumentos utilizados
-a --anos # Ano ou lista de anos que vão ser analisados, separados por espaço. Argumento Obrigatório

-v --valoresNa # Valor ou lista de valores que serão ignorados na análise. Argumento Opcional

-tp --tipoQuestao # Tipo de questão dos questionários que vão ser gerados os relatórios. Argumento Obrigatório 

-c --cursosEspecificos # Filtro do dataset usando código geral dos cursos, usando como base o Cine Rótulo. Argumento Opcional
```

## Arquivos
Para realizar os cálculos vão ser baixados arquivos referente aos microdados do(s) ano(s) escolhido(s) e também do Conceito Enade para ser usado nos cálculos estatísticos.

O projeto é divido em dois diretórios, os modulos e as operações. 

Os modulos são onde as tabelas são exportadas ou importadas e passadas para a sua devida operação. 

As operações são onde as tabelas são modificadas para realizar operações estatísticas ou gerar conteúdo importante para análise, como gráficos por exemplo.

Depois de realizadas as operações serão geradas tabelas no diretório "tabelas_criadas" e gráficos no diretório "figuras".



## Tecnologias Utilizadas

- Python
- Pip

## Autores

Projeto foi desenvolvido como parte de um TCC da UFPB - Universidade Federal da Paraíba (CAMPUS IV), do curso de Sistemas de Informação.

- Aluno: [Ricardo Ullysses Macedo Viana Filho](#https://github.com/Ricardo-Viana)
- Orientador: [Marcus Williams Aquino de Carvalho](#https://github.com/marcuswac)