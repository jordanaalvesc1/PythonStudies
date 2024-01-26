frase = 'O python é uma linguagem de programação ' \ 
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'


i = 0
qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes + ''
while i < len(frase):
     letra_atual = frase [i]
     i += 1
     continue


    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qnt_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

     

print(
    'A letra que apareceu mais vezes foi'
    f'{letra_apareceu_mais_vezes}' que apareceu'
    f'{qnt_apareceu_mais_vezes}' x)
