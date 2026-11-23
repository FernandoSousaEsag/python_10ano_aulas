import os
os.system("cls")  # limpar o ecrã do terminal (funciona no Windows)

import random
numero = random.randint(0, 100)
valor_utilizador = int(input("Adivinhe o número entre 0 e 100: "))

tentativas = 1
while valor_utilizador != numero:
    if valor_utilizador < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")
    
    print(f"Tentativa {tentativas}: {valor_utilizador} não é o número sorteado.")
    tentativas += 1
    valor_utilizador = int(input("Tente novamente: "))

print(f"Acertou !!! Número sorteado: {numero}")