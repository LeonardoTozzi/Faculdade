email = input("Informe seu email: ")
nota = float(input("Informe a nota semestral: "))
if nota > 8.5:
    print(f"Enviado para {email}")
else:
    print("Nota baixa")
