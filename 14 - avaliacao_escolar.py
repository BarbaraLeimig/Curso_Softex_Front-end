# importando biblioteca pandas
import pandas as pd

# abrindo arquivo csv
table = pd.read_csv('notas_alunos.csv', sep=';')

# cálculo da média das notas e criação da coluna média
table['media'] = (table['nota_1'] + table['nota_2']) / 2

# criando coluna situação e inserindo as condições para aprovação dos alunos
table['situacao'] = ['', '', '', '']
for i in range(len(table['situacao'])):
    if table.iloc[i, 4] >= 7 and table.iloc[i, 3] <= 5:
        table.iloc[i, 5] = 'APROVADO'
    else:
        table.iloc[i, 5] = 'REPROVADO'
print(table)
print()

# salvando em novo documento
table.to_csv('alunos_situacao.csv')

# Dados a serem mostrados na tela
maior_faltas = table['faltas'].max()
print(f'Maior número de faltas: {maior_faltas}')
media_geral = table['media'].mean()
print(f'Média geral das notas dos alunos: {media_geral}')
maior_media = table['media'].max()
print(f'Maior média: {maior_media}')
