
from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask import g
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_caching import Cache
from datetime import datetime
from werkzeug.urls import url_parse
from models import *
from forms import *
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, email_validator
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


config = {"DEBUG" : True, "CACHE_TYPE" : "SimpleCache", "CACHE_DEFAULT_TIMEOUT" : 300}
app = Flask(__name__)
app.config.from_mapping(config)
app.config['SECRET_KEY'] = 'SECRET KEY HERE'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = { 'pool_size': 200, 'pool_timeout' : 300}
cache = Cache(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DB CREDENTIALS HERE'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String(128))
    image = db.Column(db.String)
    name = db.Column(db.String, index=True, unique=True)
    uuid = db.Column(db.String, index=True, unique=True)
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    contacts = db.relationship('Contact', backref='user', lazy='dynamic')

    def __init__(self, email, name, uuid):
        self.email = email
        self.name = name
        self.uuid = uuid

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Task(db.Model):
    __tablename__ = 'task'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    priority = db.Column(db.String)
    status = db.Column(db.String)
    item_type = db.Column(db.String)
    category = db.Column(db.String)
    task_note = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    
    def __init__(self, title, priority, status, item_type, category, task_note, user):
        self.title = title
        self.priority = priority
        self.status = status
        self.item_type = item_type
        self.category = category
        self.task_note = task_note
        self.user = user

    def __repr__(self):
        return f'<Tasks {self.title}>'


class Contact(db.Model):
    __tablename__ = 'contact'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String)
    telephone = db.Column(db.String)
    email = db.Column(db.String)
    image = db.Column(db.String)
    company = db.Column(db.String)
    category = db.Column(db.String)
    contact_type = db.Column(db.String)
    title = db.Column(db.String)
    notes = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, name, telephone, email, image, company, contact_type, category, title,  user, notes):
        self.name = name
        self.telephone = telephone
        self.email = email
        self.image = image
        self.company = company
        self.contact_type = contact_type
        self.category = category
        self.title = title
        self.notes = notes
        self.user = user    
    
    def __repr__(self):
        return f'<Contacts {self.name}>'


    def contact_list(id):
        contacts = db.session.query(Contact, User).join(User).filter(Contact.user_id == id)
        return contacts 

    def get_user_with_contacts(id):
        contact = Contact.query.filter_by(user_id=id)
        id = [user.user_id for user in contact] 
        if len(id) != 0:
            return Contact.contact_list(id[-1])
        else:
            return None 


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    remember_me = BooleanField('Remember me')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email  = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            return ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationError('Please use a different e-mail.')

  
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image = FileField()
    category = StringField('Category', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    contact_type = StringField('Contact Type', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    notes = TextAreaField('Notes', validators=[DataRequired()])
    save = SubmitField('Save')


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    item_type = StringField('Item Type', validators=[DataRequired()])
    priority = StringField('Priority', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()]) 
    category = StringField('Category', validators=[DataRequired()])
    task_note = TextAreaField('Task', validators=[DataRequired()])
    save = SubmitField('Save')


      
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):  
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index', next=request.endpoint)
        return redirect(next_page)
    return render_template('login.html', title='Sign in',  form=form)          

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
       return redirect(url_for('index'))
   form = RegistrationForm()
   if form.validate_on_submit():
       user = User(name=form.name.data, email=form.email.data, uuid=uuid.uuid4().hex)
       user.set_password(form.password.data)
       db.session.add(user)
       db.session.commit()
       flash('You\'re registered')
       return redirect(url_for('login'))
   return render_template('register.html', title='Register', form=form)     


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = ContactForm()
    contacts = Contact.get_user_with_contacts(current_user.get_id())
    user_id = User.query.filter_by(id=current_user.get_id()).first()
    if request.method == 'POST' and form.validate_on_submit():
        contact = Contact(
            name = request.form.get('name'),
            image = 'default.png',
            telephone = request.form.get('telephone'),
            email = request.form.get('email'),
            category = request.form.get('category'),
            notes = request.form.get('notes'),
            company = request.form.get('company'),
            contact_type = request.form.get('contact_type'),
            title = request.form.get('title'),
            user = user_id
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', contacts = contacts, form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    form = ContactForm()
    return render_template('dashboard.html', form=form)

@app.route('/create/task', methods=['GET', 'POST'])
@login_required
def task():
    form = TaskForm()
    user_id = User.query.filter_by(id=current_user.get_id()).first()
    if form.validate_on_submit():
       task = Task(
            title = request.form.get('title'),
            item_type = request.form.get('item_type'),
            priority = request.form.get('priority'),
            status = request.form.get('status'),
            category = request.form.get('category'),
            task_note = request.form.get('task_note'),
            user = user_id
       )
       db.session.add(task)
       db.session.commit()
       return redirect(url_for('task'))  
    contacts = Contact.get_user_with_contacts(current_user.get_id())   
    return render_template('task.html', contacts = contacts, form=form)

@app.route('/view/task/<id>')
@login_required
def view_task():
    pass

@app.route('/view/tasks/<int:id>')
@login_required
def view_tasks(id):
    tasks = Task.query.filter_by(user_id=id)
    contacts = Contact.get_user_with_contacts(current_user.get_id())
    return render_template('tasks.html', tasks=tasks, contacts = contacts)

@app.route('/remove/task/<id>')
@login_required
def remove_task(id):
    removed_item = task.query.filter_by(id=id).delete()
    return Response({'status': 200})


@app.route('/create/contact')
@login_required
def contact():
    pass

@app.route('/view/contact/<id>', methods=['GET', 'POST'])
@login_required
def view_contact(id):
    contact = Contact.query.filter_by(id=id)
    contacts = Contact.get_user_with_contacts(current_user.get_id())
    return render_template('contact.html', contact = contact, contacts = contacts)

@app.route('/edit/contact', methods=['GET', 'POST'])
@login_required
def edit_contact():
    form = ContactForm()
    contacts = Contact.get_user_with_contacts(current_user.get_id())
    if request.method == 'POST':
        json_data = request.get_json()
        instance = Contact.query.filter(Contact.user_id==current_user.get_id())
        data=instance.update(dict(json_data))
        db.session.commit()
        return redirect(url_for('edit_contact'))
    return render_template('index.html', contacts = contacts, form=form)    

    
@app.route('/view/contacts')
@login_required
def view_contacts():
    contacts = Contact.get_user_with_contacts(current_user.get_id())
    return render_template('contacts.html',  contacts = contacts)


if __name__ == '__main__':
    app.run()

