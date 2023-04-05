from ZODB import FileStorage,DB
import transaction

storage = FileStorage.FileStorage('zodb/meubd.fs')
banco=DB(storage)
connection=banco.open()
root=connection.root()

print("banco de dados criado")