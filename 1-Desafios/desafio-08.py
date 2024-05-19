print('{:=^20}'.format('08'))
#coleta quantos metros são
m = float(input('Digite a quantidade de metros que queira converter em centímetros e milímetros: '))

c = m * 100
mi = m * 1000

print('{} metros são {} centímetros.'.format(m, c), '\n{} metros é igual a {} milímetros.'.format(m, mi))
