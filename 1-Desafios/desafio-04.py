print('====== 04 ======')
algo = input("Digite alguma coisa: ")

try:
    float_value = float(algo)
    is_decimal = True
except ValueError:
    is_decimal = False

print("O tipo que você digitou foi armazenado como: {}".format(type(algo)))
print('É númerico?', algo.isnumeric())
print('É alfanumerico?', algo.isalnum())
print('É alfabético?', algo.isalpha())
print('É um decimal?', algo.isdecimal())
print('Contém apenas espaços?', algo.isspace())
print('Contém apenas dígitos?', algo.isdigit())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())