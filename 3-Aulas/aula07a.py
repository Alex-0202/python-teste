#ordem de calculos no python
#1. ()
#2. **
#3. *, /, //, %
#4. +, -

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1+n2
multiplicacao = n1*n2
divisao = n1/n2
divisao_inteira = n1//n2
exponenciacao = n1**n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão inteira {} e potência {}'.format(divisao_inteira, exponenciacao))
