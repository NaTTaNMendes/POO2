from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
banco = os.path.join(path, 'pessoa.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
