qtd_prdt = int(input("Quantos produtos deseja aumentar o preço? "))
condicao = 0
maior_pç_reais = 0
maior_pç_percentual = 0

while condicao < qtd_prdt:
    print(f"{condicao+1}º produto")
    pç_atual = float(input("Digite o preço atual: R$ ").replace(',','.'))
    pç_ajustado = float(input("Digite o preço com o ajuste: R$ ").replace(',','.'))
    
    pç_reais = pç_ajustado - pç_atual # Valor do aumento em reais
    amt_percentual = pç_reais / pç_atual * 100 # Valor do aumento em percentual

    if pç_reais > maior_pç_reais: # Teste logico para determinar o maior aumento em reais.
        maior_pç_reais = pç_reais
        produto_rs = condicao+1

    if amt_percentual > maior_pç_percentual: # Teste logico para determinar o maior aumento percentual.
        maior_pç_percentual = amt_percentual
        produto_prc = condicao+1
    
    condicao += 1
    

print(
    f"O maior aumento em reais foi de R${maior_pç_reais:.2f} no {produto_rs}º produto\n"
    f"O maior aumento percentual foi de {maior_pç_percentual:.1f}% no {produto_prc}º produto".replace('.',',')
)

