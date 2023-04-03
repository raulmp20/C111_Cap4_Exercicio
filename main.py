import numpy as np

#Exercicio 1
arry1 = np.linspace(0,1,21)
print(arry1)

#Exercicio 2
pares1 = np.array([num for num in range(0,51,2)])
print(pares1)

pares2 = np.array([num for num in range(100,50,-2)])
print(pares2)

ordem = np.concatenate((pares1,pares2))
ordem = np.sort(ordem)
print(ordem)

#Exercicio 3
decres = np.flip(ordem)
print(decres)

#Exercicio 4
uns = np.ones((3,4))
array_uns = uns.flatten()
print(array_uns)

#Exercicio 5
matriz = np.ones((4,5))
num_linhas, num_colunas = matriz.shape
produto = num_linhas * num_colunas
print(produto)
if produto % 2 == 0:
    print("A matriz pode se tornar um vetor com número par de elementos")
else:
    print("A matriz pode se tornar um vetor com número ímpar de elementos")