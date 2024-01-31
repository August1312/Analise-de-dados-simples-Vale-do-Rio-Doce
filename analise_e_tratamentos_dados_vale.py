from matplotlib import pyplot as plt
import pandas as pd
# TODO: installar o Pyarrow

# Importa arquivo CSV
vale_df = pd.read_csv('Vale3.csv')

# Cria novo DataFrame com colunas específicas
vale3_resumo = vale_df[['DATA', 'FECHAMENTO']].copy()
vale3_resumo.columns = ['Data', 'Fechamento']

# Tratamento de dados para cálculos
'''
O método str.replace(',', '.') é aplicado à série.
Isso substitui todas as vírgulas (,) por pontos (.) na coluna 'Fechamento'.
Essa operação é útil quando os valores estão no formato de número decimal com vírgula como separador decimal,
 mas seu código pode exigir que os números estejam no formato com ponto como separador decimal.
O método astype(float) é aplicado à série resultante da etapa anterior. Isso converte os valores da série para o tipo de dados float.
'''
vale3_resumo['Fechamento'] = vale3_resumo['Fechamento'].str.replace(',', '.').astype(float)

# Exporta o DataFrame para um novo arquivo CSV tratado
vale3_resumo.to_csv('Vale3_resumo.csv', index=False)

# Análise dos preços médios no período dos dados selecionados
preco_medio = vale3_resumo['Fechamento'].mean()  # mean calcula a média
preco_maximo = vale3_resumo['Fechamento'].max()
preco_minimo = vale3_resumo['Fechamento'].min()

# Tratamento das Datas do DataFrame e Formatação para utilização no matplotlib
vale3_resumo['Data'] = pd.to_datetime(vale3_resumo['Data'], format="%d/%m/%Y")
'''
A linha de código que você forneceu está usando a função loc para
 obter a linha correspondente ao valor mínimo na coluna 'Fechamento' do DataFrame
 com base no índice obtido na etapa anterio
idxmin é um método que retorna o índice do primeiro valor mínimo encontrado.
'''
data_maxima = vale3_resumo.loc[vale3_resumo['Fechamento'].idxmax(), 'Data']
data_minima = vale3_resumo.loc[vale3_resumo['Fechamento'].idxmin(), 'Data']

# Calculo De Lucros ou Prejuizio caso tenha feito compra das açoes
quantidade_acoes_adquiridas = int(input('Digite a Quantidade de Ações da Vale que você comprou: '))
data_calculo = int(input('Digite Quantos dias Pretende segura as Acões antes da venda: '))
preco_aquisicao = vale3_resumo.iloc[0]['Fechamento']
data_venda = vale3_resumo.iloc[data_calculo]['Data']
preco_venda = vale3_resumo.iloc[data_calculo]['Fechamento']

valor_investido = quantidade_acoes_adquiridas * preco_aquisicao
valor_venda = quantidade_acoes_adquiridas * preco_venda

lucro_prejuizo = valor_venda - valor_investido

# Grafico de evolução dos preços
plt.figure(figsize=(12,6))
plt.plot(vale3_resumo['Data'], vale3_resumo['Fechamento'], label='Preço de Fechamento', color='blue')
plt.title('Preço Fechamento da VALE3 ao longo do período de analise')
plt.xlabel('Data')
plt.ylabel('Fechamento')
plt.legend()
plt.grid(True)
plt.show()

print(f'\nO Preço Minimo dos Dados analisados foi de exatamente R$:{preco_minimo:.2f} na Data de {data_minima} ')
print(f'\nO Preço Maximo dos Dados analisados  foi de exatamente R$:{preco_maximo:.2f} na Data de {data_maxima}')
print(f'\nSe Você tive comprado {quantidade_acoes_adquiridas} de Ações no Dia {data_minima} no valor de R$:{preco_aquisicao}')
print(f'Voce teria exatamente No final dos dados coletado por {data_calculo} Dias um {"Lucro" if lucro_prejuizo > 0 else "Prejuizo"} de R$:{abs(lucro_prejuizo):.2f} Hoje.\n')





