numeros = [0]
cont = 0
for a in range(30):
    numero = int(input(f"Digite o {a+1}º número: "))
    numeros.append(numero)

outro_numero = int(input("Agora, digite outro número qualquer: "))
for num in numeros:
    if num == outro_numero:
        cont += 1
print(f"O núméro {outro_numero} aparece {cont} vezes no vetor.")