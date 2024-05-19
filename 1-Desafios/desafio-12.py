print('{:=^20}'.format('12'))

preco = float(input('Digite o preço do produto: R$'))

desconto = preco * 0.05

novo_preco = preco - desconto

print('O valor R${} com 5% de desconto é R${:.2f}'.format(preco, novo_preco))
print('O desconto foi de {:.2f}'.format(desconto))