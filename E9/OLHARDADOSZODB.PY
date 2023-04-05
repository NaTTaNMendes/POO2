from ZODB import FileStorage,DB
import transaction
from modelo import Compania
storage = FileStorage.FileStorage('zodb/meubd.fs')
banco=DB(storage)
connection=banco.open()
root=connection.root()

# percorrer as pessoas
for pe in root['empresas']:
    print(pe)

connection.close()