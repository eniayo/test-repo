from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:eniayo1998@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.descriptioin}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.form.get('description', '')
  todo = Todo(description=description)
  db = SQLAlchemy(Flask(__name__))
  try:
      db.session.add(todo)
      db.session.commit()
  except exc.IntegrityError:
      db.session.rollback()
  return redirect(url_for('index'))

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all()
  )
