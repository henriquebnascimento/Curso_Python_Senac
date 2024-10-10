import requests

#URL da API
url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'  #ENDPOINT

# Fazendo a requisição GET para a API
response = requests.get(url)

# Verificando o status da requisição
#print(response)
if response.status_code == 200: # SE A MINHA REQUISIÇÃO FOR SATISFEITA, RETORNA O STATUA CODE 200
    jogadores = response.json() # Convertendo a resposta em formato JSON
    print(jogadores)
    for i in jogadores:
        if i['descricao'] == '5 acertos':
            print(i)
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")