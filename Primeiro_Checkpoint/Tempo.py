ano = int(input("Digite a idade atual (ano(s)): "))
mes = int(input("Digite a idade atual (mês(es)): "))
tempo = int(input("Digite a quantidade de meses para calcular a idade futura ou passada: "))
condicao = input("Digite \"F\" para calcular idade futura ou \"P\" para idade passada: ").upper()
idade_meses = (ano * 12) + mes


if condicao == "F":
    idade_meses += tempo
    ano = idade_meses // 12
    mes = idade_meses % 12
    print(f"De agora a {tempo} mês(es) o objeto de calculo terá {ano} ano(s) e {mes} mês(es).")

elif condicao == "P":
    idade_meses -= tempo
    ano = idade_meses // 12
    mes = idade_meses % 12
    print(f"À {tempo} mês(es) o objeto de calculo tinha {ano} ano(s) e {mes} mês(es).")
