# Python - 10.º ano

Exemplos de programação e exercícios em Python para os alunos.

## Exemplos

### 1) Variáveis e operações

```python
nome = "Ana"
idade = 15
media = (14 + 16 + 15) / 3

print(f"Aluno: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media:.1f}")
```

### 2) Condições (`if/elif/else`)

```python
nota = 13

if nota >= 18:
    print("Excelente")
elif nota >= 10:
    print("Aprovado")
else:
    print("Reprovado")
```

### 3) Ciclos (`for` e `while`)

```python
print("Contagem com for:")
for numero in range(1, 6):
    print(numero)

print("Contagem com while:")
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
```

### 4) Listas e funções

```python
def calcular_media(valores):
    return sum(valores) / len(valores)

notas = [12, 15, 17, 14]
resultado = calcular_media(notas)
print(f"Média da turma: {resultado:.1f}")
```

## Exercícios

1. Escreve um programa que peça o nome e a idade de um aluno e mostre uma mensagem de boas-vindas.
2. Cria um programa que leia três notas e calcule a média final.
3. Faz um programa que mostre os números de 1 a 20 e, no final, indique quantos são pares.
4. Cria uma função que receba uma lista de números e devolva o maior valor.
5. (Desafio) Faz um jogo em que o utilizador tenta adivinhar um número entre 1 e 50.