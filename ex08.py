nome_usuario = []
senha_usuario = []
for x in range(5):
    nomes = input("Digite seu nome: ")
    senhas = input("Agora, digite sua senha: ")
    nome_usuario.append(nomes)
    senha_usuario.append(senhas)
for y in range(5):
    print(nome_usuario[y], senha_usuario[y])