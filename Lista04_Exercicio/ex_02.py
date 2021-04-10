contador = 1
alunos = int(input("Quantidade de Alunos: "))
nota = 0
soma = 0

while contador <= alunos:
    nota = float(input("Nota: "))
    soma += nota
    contador += 1

print(soma / alunos)


"""
2. Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
determinar a média das notas dessa turma. Considere que o usuário digite as informações
corretamente.
"""