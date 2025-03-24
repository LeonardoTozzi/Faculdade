rm = input("Digita seu rm: ")
idade = int(input("Digita sua idade: "))

if idade >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}!")
    print("Mais informações serão enviadas ao seu e-mail cadastrado.")
else:
    autorizado = input("Você possui autorização dos responsáveis para participar? (s/n): ")
    print(autorizado)
    if autorizado == "s":
        print(f"Sua participação foi autorizada, aluno de RM {rm}!")
        print("Mais instruções serão enviadas ao email dos seus responsáveis")
    else:
        print("Sua participação não foi autorizada por causa da sua idade")
    
