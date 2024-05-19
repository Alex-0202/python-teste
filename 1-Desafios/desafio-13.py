print('{:=^20}'.format('13'))

salario_base = float(input('Digite o valor do salario: R$'))

aumento = salario_base * 0.15

novo_salario = salario_base + aumento

print('R${} salario atual.\nAumento de R${}\nO seu novo sálario é de R${:.2f}, visto que teve o aumento de 15%'.format(salario_base, aumento,novo_salario ))
