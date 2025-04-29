'''
Estruturas condicionais
if, else, elif

'''

idade = 3


# Estrutura condicional if, em C
# if(idade < 18) {
#   print('Menor de idade');
# }

if idade < 18:
  print('Menor de idade')
  
elif idade == 18:
  print('Tem 18 anos')
  
else:
  print('Maior de idade')