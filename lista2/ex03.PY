from datetime import date

nm = input("Qual o seu nome? ").strip().title()
dtn = int(input("Em que ano você nasceu? ").strip())

dtAtual = date.today()
idade = dtAtual.year - dtn


print(f"{nm} tem ou terá {idade}!")