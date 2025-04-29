# 6. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

num = int(input('Informe um número Inteiro: '))
if num % 2 == 0:
  print(f'O número {num} é PAR!')

else:
  print(f'O número {num} é Ímpar!')