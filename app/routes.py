from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Employee

main = Blueprint('main', __name__)

@main.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@main.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        email = request.form['email']

        new_employee = Employee(name=name, department=department, email=email)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_employee.html')


@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.department = request.form['department']
        employee.email = request.form['email']
        
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update_employee.html', employee=employee)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('main.index'))