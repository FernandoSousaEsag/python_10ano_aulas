import os
os.system("cls")  # limpar o ecrã do terminal (funciona no Windows)

# Ler numeros para um vector (lista) e imprimir os valores guardados no vetor

# definir um vector (lista) vazio para armazenar os números
numeros = []

for i in range(5):
    numero = int(input(f"Introduza o {i + 1}.º número: "))
    numeros.append(numero) # adiciona numero ao vector

print("Valores guardados no vetor:")

for numero in numeros:
    print(numero)