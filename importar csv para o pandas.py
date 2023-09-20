#-------Importação de bibliotecas-------

import pandas as pd
import requests
import json

# Nome do arquivo CSV
csv_file = 'SDW2023.csv'    

# -------Leitura do arquivo CSV------

# df aka data frame
#`pd.read_csv()` pandas function to read data
df = pd.read_csv(csv_file)

# Exibir os primeiros registros
#print(df.head())

#-------Filtragem de Dados-------
#declara variavel que aloca User IDs
ids_usuarios = df['UserID']

#-------Requisições HTTP para uma API-------
    #URL base da API
url_base= "https://sdw-2023-prd.up.railway.app/users/"

    #Iteração sobre os Users ID
dados_usuarios=[]
for id_usuario in ids_usuarios:
    
        url_request =f"{url_base}/usuarios/{ids_usuario}"

#fazer GET request à API
response = request.get(url_request)

# Verificar Status code da resposta
if response.status_code == 200:
    dados_usuarios.append(response.json())
else:
    
    print(f"Erro ao obter dados para o ID {id_usuario}.")
    
    
    
    
    
    
#-------Manipulação de Respostas e Dados-------


