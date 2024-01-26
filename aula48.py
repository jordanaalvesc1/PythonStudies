# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
        # 01234
        #-4321
# string = 'ABCDE' #5 caracteres
# lista =[123, True, 'Luiz Otávio', 1.2,[]]
# lista[2] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

# Create Red Update Delete
# Criar, ler, alterar, apagar = lista [i] (CRUD)

# lista = [10, 20, 30, 40, 50, 60]
# # lista[2] = 300
# # del lista[2]
# # print(lista) 
# # print(lista[2])
# lista.append(70)
# lista.pop()
# print(lista)

# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista [-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
# print(lista_d)

# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutável)

# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

Lista_a = ['Luiz', 'Maria', 1, 2]
lista_b = Lista_a.copy()

Lista_a[0] = 'Qualquer coisa'
print(Lista_a)
print(lista_b)