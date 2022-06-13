class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    levon = Mutante(nome='Levon')
    moreira = Homem(levon, nome='Moreira')
    print(Pessoa.cumprimentar(moreira))
    print(id(moreira))
    print(moreira.cumprimentar())
    print(moreira.nome)
    print(moreira.idade)
    for filho in moreira.filhos:
        print(filho.nome)
    moreira.sobrenome = 'Azevedo'
    del moreira.filhos
    moreira.olhos = 1
    del moreira.olhos
    print(levon.__dict__)
    print(moreira.__dict__)
    print(Pessoa.olhos)
    print(moreira.olhos)
    print(levon.olhos)
    print(id(Pessoa.olhos), id(moreira.olhos), id(levon.olhos))
    print(Pessoa.metodo_estatico(), levon.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), levon.nome_e_atributo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(levon, Pessoa))
    print(isinstance(levon, Homem))
    print(levon.olhos)
    print(levon.cumprimentar())
    print(moreira.cumprimentar())
