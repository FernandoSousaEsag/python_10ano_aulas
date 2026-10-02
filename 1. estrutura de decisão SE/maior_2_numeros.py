import os
os.system("cls")  # limpar o ecrã do terminal 

# Ler 2 números e determinar qual é o maior
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")
    