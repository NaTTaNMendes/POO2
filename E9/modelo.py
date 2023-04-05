from config import *
from ZODB import FileStorage,DB
import transaction
from CompaniaZODB import Companhia

class Compania(db.Model):
    id = db.Column('n', db.Integer, primary_key=True)
    nome = db.Column('name',db.String(254))
    dominio = db.Column('domain',db.String(254))
    ano = db.Column('year founded', db.String(254))
    industria = db.Column('industry',db.String(254))
    tamanho = db.Column('size range', db.String(254))
    localizacao = db.Column('locality', db.String(254))
    pais = db.Column('country', db.String(254))
    linkedin = db.Column('linkedin url', db.String(254))
    empregados_atual = db.Column('current employee estimate', db.String(254))
    empregados_total = db.Column('total employee estimate', db.String(254))

if __name__ == "__main__":

    storage = FileStorage.FileStorage('zodb/meubd.fs')
    banco=DB(storage)
    connection=banco.open()
    root=connection.root()

    # Adiciona o laranja

    
    comp = Companhia(id=1, nome="teste", dominio="teste", ano="teste", industria="teste", tamanho="teste", localizacao="teste", pais="teste", linkedin="teste", empregados_atual="teste", empregados_total="teste")
    root['empresas'] = [comp]
    empresas = root['empresas']
    #transaction.commit()
    
    n = 1
    for c in db.session.query(Compania).limit(100000):
        #print(n, c.id, c.nome)
        temp = Companhia(c.id, c.nome, c.dominio, c.ano, c.industria, c.tamanho, c.localizacao, c.pais, c.linkedin, c.empregados_atual, c.empregados_total)
        
        #empresas = root['empresas']
        empresas.append(temp)
        #root['empresas'] = empresas

        #empresas.append(temp)
        #transaction.commit()

        n+=1
    root['empresas'] = empresas
    transaction.commit()
    
    # exibindo apenas 10 registros
    #n = 1        
    #for c in db.session.query(Compania).limit(10):
    #    print(n, c.id, c.nome)
    #    n+=1
    # exibindo apenas registros entre 6 e 8
    #n = 1        
    #for c in db.session.query(Compania).offset(5).limit(3):
    #    print(n, c.id, c.nome)
    #    n+=1
    connection.close()