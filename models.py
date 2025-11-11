from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  completed = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default=datetime.now())

  def __repr__(self):
    return '<Task %r>' % self.id