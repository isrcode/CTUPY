condicao = input("Gostaria de inserir as medidas? S/N ").upper()

while condicao == "S":
	a = float(input("Primeira medida: "))
	b = float(input("Segunda medida: "))
	c = float(input("Terceira medida: "))

	if a + b < c:
		print("Estás medidas não formam um triangulo!")
	elif a + c < b:
		print("Estás medidas não formam um triangulo")
	elif b + c < a:
		print("Estás medidas não formam um triangulo")
	else:
		p = (a + b + c) / 2

		area = (p * (p-a) * (p-b) * (p-c)) ** 0.5
		print(f"A área do triangulo é {area:.2f}")
			
		condicao = input("Gostaria de inserir novas medidas? S/N ").upper()
else:
    print("Fim do programa!")
