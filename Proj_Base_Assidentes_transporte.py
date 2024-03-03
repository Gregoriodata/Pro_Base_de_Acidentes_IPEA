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

#url_serie = f'https://www.ipea.gov.br/atlasviolencia/api/v1/serie/{tema_id}'

url_valor = f'https://www.ipea.gov.br/atlasviolencia/api/v1/valores-series/{serie_id}/{abrangencia}'



requisicao = rq.request("GET",url_valor)  #Requisição API metodo GET
print(requisicao) #Teste Requisição API
retor_requi = json.loads(requisicao.text) #Converter os dados em dicionario text - metodo 

print(type(retor_requi))

# df = pd.DataFrame(retor_requi) 
# print(df)

# df2 = df['sigla']
# df2 = df2.drop_duplicates()
# print(df2)
# df.to_csv('tbl.csv')
# df.to_parquet('df.parquet.gzip',compression='gzip')


# print(len(retor_requi)) #Tamanho da lista
# print(retor_requi[:1])

# dim_UF = []  #Dimensão localidade 
# print(type(dim_UF))

# for i in (retor_requi):
#        if not (i['cod'], i['sigla']) in dim_UF:
#         dim_UF.append((i['cod'], i['sigla']))

# #print(dim_UF)

# print("------------------------------")

# tbl_fato = [] #Tabela de registros dos fatos ocorridos.

# for i in (retor_requi):
#     if not (i['cod'], i['valor'], i['periodo']) in tbl_fato:
#         tbl_fato.append((i['cod'], i['valor'], i['periodo']))

# print(tbl_fato)
    
# dim_date = [] # Tabela dim data

# for i in (retor_requi):
#      if not i['periodo'] in dim_date:
#          dim_date.append(i['periodo'])
# print(dim_date)