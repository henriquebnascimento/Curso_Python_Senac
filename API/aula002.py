import requests
import openpyxl

#URL da API
url = 'https://jsonplaceholder.typicode.com/users'  #ENDPOINT

# Fazendo a requisição GET para a API
response = requests.get(url)
# Verificando o status da requisição
#print(response)
if response.status_code == 200: # SE A MINHA REQUISIÇÃO FOR SATISFEITA
    useres = response.json() # Convertendo a resposta em formato JSON
    #print(useres)


    # Criando um arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active


    # Adicionando os cabeçalhos
    sheet.append(["ID","Nome","Email","Empresa"])

    # Adicionando dados da API ao Excel
    for user in useres:
        sheet.append([user['id'], user['name'], user['email'], user['company']['name']])

    # Salvando o arquivo
    workbook.save("usuarios_api.xlsx")
    print("Dados salvos no aquivos 'usuarios_api.xlsx'")
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")