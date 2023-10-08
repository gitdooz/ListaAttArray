numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Números na ordem inversa: ")
for x in range(4, -1, -1):
    print(numeros[x])
