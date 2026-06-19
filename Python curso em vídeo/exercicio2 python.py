numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite outro:'))
resultado = numero1 + numero2
# print('A soma entre', numero1, 'e', numero2, 'vale', resultado)
print('A soma entre {} e {} vale {}'.format(numero1, numero2, resultado))

print('')
# Verifica se é numérico
digitar = input('Digite alguma coisa: ')
print(digitar.isnumeric())

#Verifica se é letra
digitar2 = input('Escreva algo: ')
print(digitar2.isalpha())

#verficar se é alfa numérico
digitar3 = input('Escreva algo: ')
print(digitar3.isalnum())

#verificar se é maiúsculo
digitar4 = input('Escreva algo: ')
print(digitar4.isupper())
#verificar se é decimal
digitar5 = input('Escreva algo: ')
print(digitar5.isdecimal())