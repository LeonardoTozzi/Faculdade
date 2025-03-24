valor = float(input("Informe o valor da compra realizada: "))
cupom = input("Informe o cupom de desconto: ")

if cupom == "NIVER10":
   valor_final=float(valor)*0.9
else: 
    valor_final = float(valor)
    print("CUPOM INVÁLIDO")
print(f"O valor final da compra é {valor_final}")