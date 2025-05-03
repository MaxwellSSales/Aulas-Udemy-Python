'''
Loop for

Loop -> Estrutura de repetição.
for -> É uma dessas estruturas.

C ou java

for(int i =0; i < 10; i++) {
   //execução do loop
}

Python

for item in interavel:
   //execução do loop
   
Utilizamos loop para iterar sobre seguências ou sobre valores iteráveis

Exemplos de iteráveis:

- String
    nome = 'Geek University'
    
- Listas
    lista = [1, 3, 5, 7, 9]
    
- Range
    numeros = range(1, 10)
    
# Exemplo de for 1 (Iterando sobre uma string)

for letra in nome:
    print(letra)
  
# Exemplo de for 2 (Iterando sobre uma lista)

for numero in lista:
    print(numero)
  
# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
Obs: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)
  
enumerate:

((0, 'G', (1, 'e'), (2, 'e'), (3, 'k'), ...))

for indice, letra in enumerate(nome):
    print(nome[indice])
  
for indice, letra in enumerate(nome):
    print(letra)
  
for _, letra in enumerate(nome):
    print(letra)
  
Obs: quando não pecisamos de um valor podemos descartá-lo utilizando um inderline (_).

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)
  
qtd = int(input('quantas vezes esse loop deve rodar? '))
soma =0

for num in range(1, qtd + 1):
    num - int(input(f'Informe o {num}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end=' ')

'''

# Original: U+1F970
# Modificado: U0001F970

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F970' * num)