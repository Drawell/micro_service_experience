import os

from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = os.getenv("DB_PASSWORD", "debug_secret")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    tasks = Task.query.order_by(Task.create_date.desc()).all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if title:
        new_task = Task(
            title=title, 
            description=description,
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task created!', 'success')
    
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_complete_date = None if task.complete_date else datetime.now()
    task.complete_date = new_complete_date
    db.session.commit()
    flash('Task status updated!', 'info')
    return redirect(url_for('index'))


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
            
        db.session.commit()
        flash('Task edited!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)