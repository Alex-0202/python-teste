print('{:=^20}'.format('10'))
real = float(input('Quantos reis você possui na carteira? R$'))

conversao = real/5.10

print('Você pode comprar ${:.2f} dólares com R${} reais'. format(conversao, real))
