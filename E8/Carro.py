from Conexao import *
from Pessoa import *

class Carro(db.Model):
    plate = db.Column(db.String(7), primary_key=True)
    name = db.Column(db.String(250))
    color = db.Column(db.String(20))
    model_year = db.Column(db.Integer)
    
    pessoa_cpf = db.Column(db.Integer, db.ForeignKey(Pessoa.cpf))
    pessoa = db.relationship("Pessoa")

    def __str__(self):
        return f"[{self.plate}], {self.name}, {self.color}, {self.model_year}, {self.pessoa}"
    
    