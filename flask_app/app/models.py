from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    complete_date = db.Column(db.DateTime, default=None)
    
    def __repr__(self):
        return f'<Task {self.title}>'
