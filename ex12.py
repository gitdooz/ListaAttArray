nomes = []
inverso = []
for i in range(5):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)
print(f"Os nomes são:{nomes}")
print("Agora, os nomes na ordem inversa: ")
for y in range(4, -1, -1):
    inverso.append(nomes[y])

for nome in inverso:
    print(nome, end=". ")


