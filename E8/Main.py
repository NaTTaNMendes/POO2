from Pessoa import *
from Carro import *
from Conexao import *
from datetime import date

# apagar o arquivo, se houver
if os.path.exists(banco):
    os.remove(banco)

# criar tabelas
db.create_all()

# criar pessoas
p1 = Pessoa(cpf=12365455670, name="Nattan Mendes Tinonin", email="nattan078@gmail.com", birth_date=date(2003, 10, 17))   
  
db.session.add(p1)
db.session.commit()

c1 = Carro(plate="BCH321H", name="Fiat Uno", color="Preto", model_year=2012, pessoa=p1)

db.session.add(c1)
db.session.commit()

print(c1)