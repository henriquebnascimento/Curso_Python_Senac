import requests

#URL da API
url = 'https://jsonplaceholder.typicode.com/users'  #ENDPOINT

# Fazendo a requisição GET para a API
response = requests.get(url)

# Verificando o status da requisição
#print(response)
if response.status_code == 200: # SE A MINHA REQUISIÇÃO FOR SATISFEITA
    useres = response.json() # Convertendo a resposta em formato JSON
    #print(useres)
    
    for user in useres:
        #if user['id'] == 1:
            print(f"Id: {user['id']}, Nome: {user['name']}, Email: {user['email']}, Telefone: {user['phone']}")
                      
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")