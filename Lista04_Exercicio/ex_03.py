contador = 1
alunos = int(input("Quantidade de Alunos: "))
nota = 0
soma = 0
abaixo5 = 0
acima5 = 0

while contador <= alunos:
    nota = float(input("Nota: "))
    if nota <= 5:
        abaixo5 += 1
    else:
        acima5 += 1        
    soma += nota
    contador += 1

print(soma / alunos)
print(
    f"{acima5} Alunos tiram mais de 5.\n"
    f"{abaixo5} Alunos tiram menos de 5."
)

"""
2. Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
determinar a média das notas dessa turma. Considere que o usuário digite as informações
corretamente.
3. Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5, 0
( 0 ≤ nota < 5, 0 ) e acima de 5, 0 ( nota ≥ 5, 0 ).

"""