# Quando queremos um conjunto de dados imutaveis.
# Ou seja, dados que começaram daquela forma ex: nome, idade, cep
# Nesse caso usamos a tupla (nome, idade, cep)

def lista(nome, idade, cep):
    cadastro = (f"{nome}", f"{idade}", f"{cep}")
    print(cadastro)
    print(type(cadastro))


lista('Lucas Costa Pereira', '25', '72871-049')

