def soma_pares(numeros): # criando uma função que exiba a soma dos números pares encontrados no parametro passado
    soma = 0
    i = 0
    pares = 0
    pares_encontrados = []
    while i < len(numeros):
        if numeros[i] % 2 == 0:
            pares_encontrados.append(numeros[i])
            pares += 1
            soma += numeros[i]
        i += 1
    print(f'Total de números pares encontrados: {pares}')
    print(f'Números pares: {pares_encontrados}')
    print(f'Soma dos números pares encontados: {soma}')
soma_pares([1,2,3,4,5,6,8,10,21,17,16,])