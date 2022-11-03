# Criando uma API para retornar dados de servidores públicos da UFC

 - Base de dados 
 
 Lendo a base de dados:
```python
import pandas as pd
import random
url = f'https://docs.google.com/spreadsheets/d/e/2PACX-1vRgZ_FlWM5ZhQOyjdO_jASVUVkmv8IWShSxVWwWQduzPeDl5TGb5wchBGeDGq589bpW21PhKxMaY8yK/pub?gid=469198453&single=true&output=csv'
df = pd.read_csv(url)
df.drop_duplicates(inplace=True)
```
#### Função para retornar servidores aleatórios 
Função para retornar um servidor aleatório:
```python
def get_servidor_aleatorio():
	#separa apenas os nomes únicos na base de dados 
	nomes_unicos = df['nome'].unique()
	#quantifica os nomes
	qdt_nomes = len(nomes_unicos)
	#Retornando um servidor aleatório 
	return df[df['nome'].str.contains(nomes_unicos[random.randint(0,qdt_nomes-1)])==True]
``` 
#### Função para retornar servidores dado um nome
 Função para retornar um servidor dado um nome:
```python
def busca_servidor(nome):
	#Faz a busca de um nome ou parte de um nome
    return df[df['nome'].str.contains(nome)==True]
``` 


Testando as funções
```python
print(get_servidor_aleatorio())
print(busca_servidor('JOAO BOSCO DO MONTE')) 
``` 
## Código completo.
```python
import pandas as pd
import random
url = f'https://docs.google.com/spreadsheets/d/e/2PACX-1vRgZ_FlWM5ZhQOyjdO_jASVUVkmv8IWShSxVWwWQduzPeDl5TGb5wchBGeDGq589bpW21PhKxMaY8yK/pub?gid=469198453&single=true&output=csv'
df = pd.read_csv(url)
df.drop_duplicates(inplace=True)
def busca_servidor(nome):
	#Faz a busca de um nome ou parte de um nome
    return df[df['nome'].str.contains(nome)==True]
def get_servidor_aleatorio():
	#separa apenas os nomes únicos na base de dados 
	nomes_unicos = df['nome'].unique()
	#quantifica os nomes
	qdt_nomes = len(nomes_unicos)
	#Retornando um servidor aleatório 
	return df[df['nome'].str.contains(nomes_unicos[random.randint(0,qdt_nomes-1)])==True]
print(get_servidor_aleatorio())
print(busca_servidor('JOAO BOSCO DO MONTE')) 
``` 
# Criando a API