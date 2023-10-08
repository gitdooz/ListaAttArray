nome_usuario = []
senha_usuario = []
print("__________LOGIN__________")
for x in range(5):
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    nome_usuario.append(nome)
    senha_usuario.append(senha)
for y in range(5):
    print(f"{nome_usuario[y]}, seu login foi efetuado com sucesso!")