from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Task


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' 
db.init_app(app)

@app.route("/", methods=['POST', 'GET'])
def index():

  if(request.method == 'POST'):
    newTask = Task(content=request.form['content'])

    try:
      db.session.add(newTask)
      db.session.commit()
      return redirect('/')
    except:
      print('An exception occurred')

  else:
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

# TODO - ADICIONAR OUTRAS ROTAS/MÉTODOS/FUNCIONALIDADES


app.run(debug=True)