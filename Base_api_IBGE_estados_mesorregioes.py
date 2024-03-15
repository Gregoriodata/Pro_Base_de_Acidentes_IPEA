import requests as rq
import json as js
import pandas as pd
def dim_localidade ():
    url_Valor = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/?/mesorregioes'
    req = rq.request("GET",url_Valor)
    ret_req = js.loads(req.text)

    df = pd.DataFrame(ret_req)
    df_dim_localidade = df[['id','sigla','nome']]

    df_dim_localidade.to_csv('Dim_localidade.csv')
    return df_dim_localidade

