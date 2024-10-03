def soma_pares(numeros):
    soma = 0
    i = 0
    pares_encontrados = []
    while i < len(numeros):
        if numeros[i] % 2 == 0:
            pares_encontrados.append(numeros[i])
            soma += numeros[i]
        i += 1
    print(f'Pares encontrados: {pares_encontrados}')
    print(f'A soma dos pares encontrados é: {soma}')
soma_pares([1,2,3,4,5,6,7,8,9])