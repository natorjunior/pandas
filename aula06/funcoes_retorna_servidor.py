import pandas as pd
import random
url = f'https://docs.google.com/spreadsheets/d/e/2PACX-1vRgZ_FlWM5ZhQOyjdO_jASVUVkmv8IWShSxVWwWQduzPeDl5TGb5wchBGeDGq589bpW21PhKxMaY8yK/pub?gid=469198453&single=true&output=csv'
df = pd.read_csv(url)
df.drop_duplicates(inplace=True)

def get_servidor_aleatorio():
    nomes_unicos = df['nome'].unique()
    qdt_nomes = len(nomes_unicos)
    return df[df['nome'].str.contains(nomes_unicos[random.randint(0,qdt_nomes-1)])==True]
def busca_servidor(nome):
    return df[df['nome'].str.contains(nome)==True]
print(get_servidor_aleatorio())
print(busca_servidor('JOAO BOSCO DO MONTE'))