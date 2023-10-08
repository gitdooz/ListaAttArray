quant_aluno = int(input("Quantos alunos tem na sala? "))
nome_aluno = [''] * quant_aluno
for i in range(quant_aluno):
    nome_aluno[i] = input("Digite o nome do aluno: ")
print(f"Alunos: {nome_aluno}")