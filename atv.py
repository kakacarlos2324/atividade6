# Criação do dicionário para armazenar os dados dos alunos
alunos = {}

# Leitura dos valores usando um loop for
for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    alunos[nome] = nota

# Cálculo da soma das notas
soma_notas = sum(alunos.values())

# Cálculo da média das notas
media = soma_notas / len(alunos)

print(f"A média das notas dos alunos é: {media:.2f}")