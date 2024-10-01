mensagem = "Hello, world"

#concatenando strings
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " "+ sobrenome
print(nome_completo)

 # Acessando caracteres idividuais
primeiro_caractere = mensagem[0]
ultimo_caractere = mensagem[-1]

# Encontrando o comprimento de uma string

mensagem = "Hello, world"
comprimento = len(mensagem)
print(comprimento)

# Encontrando um cartere específico dentro de uma string
print(mensagem.find('w'))

# Encontrando se uma substring está dentro de uma string:
mensagem = "Hello, world"
if "world" in mensagem:
    print("A substring 'world' está presente na mensagem.")

#convertendo uma substring em maiúscula e minúscula:
maiuscula = mensagem.upper()
minuscula = mensagem.lower()


#dividindo uma string em substrings com base em um delimitador
mensagem_separada = mensagem.split(",") # separa a string numa lista com base nos espaços
print(mensagem_separada)


# Convertendo a primeira letra de cada palavra em maiúscula
pri_maiuscula = mensagem.capitalize() #captalize
print(pri_maiuscula)

# Substituindo caracteres em uma string
mensagem = "Hello, world"
noma_mensagem = mensagem.replace("world", "Python") #replace
print(noma_mensagem)

mensagem = "hello, world"
primeira_linha = mensagem[2:] #pego do segundo índice em diante
h = mensagem[0] # pego o índice na posicao zero 'h'
i = mensagem[1] # pego o índice na posição um 'e'
i = i.upper() # pego o indice e converto pra maiusculo
juncao = h + i + primeira_linha
print(juncao)

# strip remove espaços em branco de uma string

# frase = '       Hello,           world      '
# frase_separada = frase.split()
# frase_junta = frase_separada
# print(frase_junta)
# print(frase_separada)
# sem_espacos = frase.strip()
# print(sem_espacos)

