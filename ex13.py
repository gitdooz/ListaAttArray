valores = [] * 5
pares = []
maior = 0
soma = 0
cont = 0
for a in range(30):
    numero = int(input(f"Digite o {a+1}º valor: "))
    valores.append(numero)
for par in valores:
    if par % 2 == 0:
        pares.append(par)
for num in valores:
    if num > maior:
        maior = num
menor = maior
for b in range(30):
    if valores[b] < menor:
        menor = valores[b]
for c in valores:
    soma += 1
media = soma/30
for d in valores:
    if d > media:
        cont += 1

print(f"Números pares: {pares}\n"
      f"_______________________\n"
      f"Maior número: {maior}\n"
      f"_______________________\n"
      f"Menor número: {menor}\n"
      f"_______________________\n"
      f"Maiores que a média: {cont}\n"
      f"_______________________")

