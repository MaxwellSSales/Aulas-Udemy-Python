'''
Escopo Variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
    
2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada.
    
Para declarar vriáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nósnão colocamos o tipo de dado nela. Esse tipo é inserido ao atribuímos o valor á mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
'''
numero = 42 # Exemplo de variavel global
print(numero)

numero = 42

if numero > 10:
  novo = numero + 10 # A variável 'novo' está declarada localmemte dentro do bloco do if. Portanto, é local 
  print(novo)
print(novo)