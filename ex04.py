notas = []
soma = 0
cont = 0
for i in range(5):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)
for x in range(5):
    soma += notas[x]
media = soma/5
for y in range(5):
    if notas[y] >= media:
        cont = cont + 1
print(f"A média da turma foi {media} e {cont} alunos obtiveram a nota maior que a média")
