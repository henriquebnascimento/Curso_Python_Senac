#if, elif e else

cupom =  str(input('Digite o cupom: '))

if (cupom == 'FUCTURA1'):
    print('Você ganhou 15% de desconto')
elif(cupom == 'FUCTURA2'):
    print('Você ganhou 10% de desconto') 
elif(cupom == 'XANDAO'):
    print('Você foi proibido de efetuar essa compra')
else:
    print('Você ganhou 5% de desconto')   
    