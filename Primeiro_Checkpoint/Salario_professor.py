num_aulas = int(input("Quantidade de aulas: "))
vl_hora_aula = float(input("Valor da Hora aula: "))

salario_base = vl_hora_aula * 4.5 * num_aulas

hora_atividade = salario_base * 0.05

dsr = (salario_base + hora_atividade) * (1/6)

sal_mensal = salario_base + hora_atividade + dsr

print(
    "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
    f"Salario base:            R$ {salario_base:.2f}\n"
    f"Valor da Hora Atividade: R$ {hora_atividade:.2f}\n"
    f"DSR:                     R$ {dsr:.2f}\n"
    f"Salario Mensal:          R$ {sal_mensal:.2f}\n"
    "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
    .replace(".",",")
)