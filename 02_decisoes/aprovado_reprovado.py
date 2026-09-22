import os
os.system("cls")  # limpar o ecrã do terminal (funciona no Windows)

nota1 = float(input("Introduza a primeira nota: "))
nota2 = float(input("Introduza a segunda nota: "))
nota3 = float(input("Introduza a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.1f}") # imprime  média com uma casa decimal

if media >= 10:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

    