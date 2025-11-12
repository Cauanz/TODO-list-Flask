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

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
  task = Task.query.get_or_404(id)

  if request.method == 'POST':
    task.content = request.form['content']

    try:
      db.session.commit()
      return redirect("/")
    except:
      print('Something went wrong when trying to update the task.')

  else:
    return render_template("update.html", task=task)


@app.route("/delete/<int:id>")
def delete(id):

  task = Task.query.get_or_404(id)

  if task:
    try:
      db.session.delete(task)
      db.session.commit()
      return redirect("/")
    except:
      print('Something went wrong when trying to delete the task.')

app.run(debug=True)