quantAlunos = int(input("Insira a quantidade de alunos: "))
nomeAluno = [""] * quantAlunos
cont = int(0)

for i in range(quantAlunos):
    nomeAluno[i] = input(f"Digite o nome do {i}º aluno: ")

pesquiseNome = input("Digite o nome que está querendo pesquisar: ")

for x in range(quantAlunos):
    if pesquiseNome == nomeAluno[x]:
        print(f"Nome do usuário é {nomeAluno[x]} na posição {x}")
    else:
        cont = cont + 1

if cont == quantAlunos:
    print("Aluno não encontrado!")


