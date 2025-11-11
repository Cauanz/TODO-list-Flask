from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' 

@app.route("/")
def index():

  # TODO - PAREI CRIANDO A FUNCIONALIDADE DESSA ROTA (QUE É EXIBIR AS TASKS SE NÃO LEMBRA)
  # TODO - E FAZER TODO RESTO

  return render_template("index.html")


app.run(debug=True)