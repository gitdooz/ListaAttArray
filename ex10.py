N = int(input("Digite um número para ser o tamanho do vetor: "))
vetor_A = []
vetor_B = []
Soma = []
for i in range(N):
     elemento = int(input("Digite: "))
     vetor_A.append(elemento)
for x in range(N):
    elemento = int(input("Digite: "))
    vetor_B.append(elemento)
for y in range(N):
    soma_elemento = vetor_A[y] + vetor_B[y]
    Soma.append(soma_elemento)

print("\nVetor Soma:")
for elemento in Soma:
    print(elemento)
