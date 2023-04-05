from Persistence import Persistent

class Companhia(Persistent):

    def __init__(self, id, nome, dominio, ano, industria, tamanho, localizacao, pais, linkedin, empregados_atual, empregados_total):
        self.id = id
        self.nome = nome
        self.dominio = dominio
        self.ano = ano
        self.industria = industria
        self.tamanho = tamanho
        self.localizacao = localizacao
        self.pais = pais
        self.linkedin = linkedin
        self.empregados_atual = empregados_atual
        self.empregados_total = empregados_total

    def __str__(self):
        return f'{str(self.id)}, {self.nome}, {self.dominio},\
                , {self.ano}, {self.industria}, {self.tamanho}\
                , {self.localizacao}, {self.pais}, {self.linkedin}\
                , {self.empregados_atual}, {self.empregados_total}'
