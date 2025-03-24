rm = input("Digita seu rm: ")
idade = int(input("Digita sua idade: "))

if int(idade) >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}!")
    print("Mais informações serão enviadas ao seu e-mail cadastrado.")
else:
    print("Sua participação não foi autorizada por causa da idade")
    
