contador = 1
alunos = int(input("Quantidade de Alunos: "))
nota = 0
soma = 0

while contador <= alunos:
    nota = float(input("Nota: "))
    soma += nota
    contador += 1

print(soma / alunos)