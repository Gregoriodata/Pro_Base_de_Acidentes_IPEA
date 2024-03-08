import requests as rq # modulo python para requisição de API
import json
import pandas as pd
# import pyarrow
# import fastparquet

###Transformar as listas em DataFrame e gerar arquivos em CSV, "Comando POP" 
# CTRL ;  -- Comenta todas as linhas

id = 1
serie_id = 85 # Óbitos em acidentes de transporte
abrangencia = 3 # Abrangência da Série. Ex: 1 - País | 2 - Região | 3 - UF | 4 - Município
tema_id = 85

url_valor = f'https://www.ipea.gov.br/atlasviolencia/api/v1/valores-series/{serie_id}/{abrangencia}'

requisicao = rq.request("GET",url_valor)  #Requisição API metodo GET
retor_requi = json.loads(requisicao.text) #Converter os dados em dicionario text - metodo 

df = pd.DataFrame(retor_requi) #Transformar dic em Data Frame


# print(type(df))


# print(df.shape) #Quantidade de linhas e colunas do DataFrame
# print(df.index) #Descrição do Index
# print(df.columns)#Colunas presentes no DataFrame
# print(df.count()) #Contagem de dados não-nulos
# print(df['cod'])#Realizando o print de uma coluna selecionada;
# print(df[['cod', 'sigla']])#Realizando o print de duas coluna selecionada;
# print(df.describe())  --- ??



# dim_UF = []  #Dimensão localidade 
# print(type(dim_UF))
# for i in (retor_requi):
#        if not (i['cod'], i['sigla']) in dim_UF:
#         dim_UF.append((i['cod'], i['sigla']))
# #print(dim_UF)
# print("------------------------------")


df_dim_Localidade = df[['cod', 'sigla']]
df_dim_Localidade = df_dim_Localidade.drop_duplicates()

print(df_dim_Localidade.count())
# print(df_dim_Localidade)

print("------------------------------") #891 x 2c / cod 27 - sigla 27 

# dim_date = [] # Tabela dim data

# for i in (retor_requi):
#      if not i['periodo'] in dim_date:
#          dim_date.append(i['periodo'])
# print(dim_date)

df_dim_Date = df['periodo']
df_dim_Date = df_dim_Date.drop_duplicates()

print(df_dim_Date.count())

print("------------------------------") #891 / 33

# tbl_fato = [] #Tabela de registros dos fatos ocorridos.
# for i in (retor_requi):
#     if not (i['cod'], i['valor'], i['periodo']) in tbl_fato:
#         tbl_fato.append((i['cod'], i['valor'], i['periodo']))
# print(tbl_fato)

df_tbl_Fato = df[['cod','valor','periodo']]
print(df_tbl_Fato.count())

print("------------------------------") #891


# df2 = df['sigla']
# df2 = df2.drop_duplicates()
# print(df2)
# df.to_csv('tbl.csv')
# df.to_parquet('df.parquet.gzip',compression='gzip')
# print(len(retor_requi)) #Tamanho da lista
# print(retor_requi[:1])
# 


    
