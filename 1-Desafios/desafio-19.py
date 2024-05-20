'''import random
alunos = []
n1 = int(input('Digite a quantidade de alunos: '))
for i in range(n1):
     nome = input('Qual é o nome do {}° aluno?'.format(i+1))
     alunos.append(nome)
aletorio = random.choice(alunos)
print('O aluno selecionado aleatoriamente é: ', aletorio)'''
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O Aluno escolhido foi {}'.format(escolhido))

