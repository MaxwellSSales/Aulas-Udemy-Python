# 4. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

num1 = int(input('Informe o Primeiro Valor Inteiro: '))
num2 = int(input('Informe o Segundo Valor Inteiro: '))

if num1 > num2:
  print(f'O primeiro número {num1} é maior')
elif num1 == num2:
  print('Os dois números são iguais!')
else:
  print(f'O segundo número {num2} é maior')