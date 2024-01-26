# Uma introdução às f-strings

nome = 'Jordana Alves'
altura = 1.58
peso = 49
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.3f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print (linha_2)
print (linha_3)

