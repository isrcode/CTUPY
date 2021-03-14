vlAvista = float(input("Qual o valor a vista? "))
vlParcela = float(input("Qual o valor da parcela? "))
"""
100 = 1000
X     970

X = 100*970
    1000

X = 97%

100 - X  = 3%

3% é o desconto para pagamento a vista no estado de São Paulo.
"""
pcDesconto = 100 - (vlAvista*100)/(vlParcela*10)  

print(f"O desconto para pagamento a vista é de {pcDesconto:.0f}%")