import os
os.system("cls")  # limpar o ecrã do terminal 

# Ler 2 números e determinar qual é o maior
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num2 = int(input("Introduza o terceiro número: "))

maior = num1;
if num2 > maior:
    maior = num2

if num2 > maior:
    maior = num3   

print(f"O maior número é: {maior}")