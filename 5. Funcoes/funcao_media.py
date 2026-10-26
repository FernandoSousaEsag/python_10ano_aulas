
import os
os.system("cls")  # limpar o ecrã

def Media(a, b, c):
    return (a + b + c) / 3


num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num3 = int(input("Introduza o terceiro número: "))

media = Media(num1, num2, num3)

print(f"A média é: {media:.2f}")