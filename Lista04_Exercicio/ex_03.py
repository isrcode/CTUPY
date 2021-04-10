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