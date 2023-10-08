numeros = []
for a in range(5):
    numero = int(input(f"Digite o {a+1}º número: "))
    numeros.append(numero)
for b in range(4, -1, -1):
    print(numeros[b], end=" ")