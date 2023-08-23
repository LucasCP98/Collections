usuarios = [
    ('Lucas', 25, 1998),
    ('Larissa', 24, 1999),
    ('Loris', 20, 2003),
]
# Caso queira ignorar, por exemplo, idade e ano_nascimento,
# basta subistuir os valores por _ anderlaine
# ex: for nome, _, _ in usuarios:
# Mas é melhor deixar explicito.
for nome, idade, ano_nascimento in usuarios:
    print(nome, idade, ano_nascimento)

