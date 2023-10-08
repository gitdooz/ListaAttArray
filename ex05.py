vetor_a = [0]
vetor_m = [0]
for a in range(10):
    num = float(input("Digite um número: "))
    vetor_a.append(num)

x = float(input("Agora, digite outro número: "))

for b in range(10):
    vetor_m = vetor_a[b] * x
print(f"O vetor M: {vetor_m}")
