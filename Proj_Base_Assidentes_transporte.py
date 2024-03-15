import requests as rq # modulo python para requisição de API
import json
import pandas as pd
import csv
import Base_api_IBGE_estados_mesorregioes as BaIBGE

id = 1
serie_id = 85 # Óbitos em acidentes de transporte
abrangencia = 3 # Abrangência da Série. Ex: 1 - País | 2 - Região | 3 - UF | 4 - Município
tema_id = 85

url_valor = f'https://www.ipea.gov.br/atlasviolencia/api/v1/valores-series/{serie_id}/{abrangencia}'
requisicao = rq.request("GET",url_valor)  #Requisição API metodo GET
retor_requi = json.loads(requisicao.text) #Converter os dados em dicionario text - metodo 
df = pd.DataFrame(retor_requi) #Transformar dic em Data Frame

BaIBGE.dim_localidade()

print("------------------------------") 
local = 'D:\Python_Projetos\Projeto_Base_de_Acidentes\Bases'
no_arqu = '\_dim_Date.csv'
df_dim_Date = df['periodo']
df_dim_Date = df_dim_Date.drop_duplicates()
df_dim_Date.to_csv(f'{local+no_arqu}')

print("------------------------------") 
no_arqu_fato = '\_tbl_Fato_.csv'
df_tbl_Fato = df[['cod','valor','periodo']]
df_tbl_Fato = df_tbl_Fato.to_csv(f'{local+no_arqu_fato}')

print("------------------------------") 
# print(type(df))
# print(df.shape) #Quantidade de linhas e colunas do DataFrame
# print(df.index) #Descrição do Index
# print(df.columns)#Colunas presentes no DataFrame
# print(df.count()) #Contagem de dados não-nulos
# print(df['cod'])#Realizando o print de uma coluna selecionada;
# print(df[['cod', 'sigla']])#Realizando o print de duas coluna selecionada;
# print(df.describe())  --- ??


    
