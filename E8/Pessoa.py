from Conexao import *

class Pessoa(db.Model):
    cpf = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(100))
    birth_date = db.Column(db.Date)

    def __str__(self):
        return f"[{self.cpf}], {self.name}, {self.email}, {self.birth_date}"
    