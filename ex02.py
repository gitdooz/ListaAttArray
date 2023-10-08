quantAlunos = int(input("Insira a quantidade de alunos: "))
nomeAluno = [""] * quantAlunos
cont = int(0)

for i in range(quantAlunos):
    nomeAluno[i] = input(f"Digite o nome do {i + 1}º aluno: ")

for x in range(quantAlunos):
    print(f"Nome do usuário é {nomeAluno[x]} na posição {x}")




