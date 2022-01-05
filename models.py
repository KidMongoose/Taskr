# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin, LoginManager
# from app import db, login_manager  


# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String, index=True, unique=True)
#     password = db.Column(db.String(128))
#     image = db.Column(db.String)
#     name = db.Column(db.String, index=True, unique=True)
#     uuid = db.Column(db.String, index=True, unique=True)
#     tasks = db.relationship('Task', backref='author', lazy='dynamic')
#     contacts = db.relationship('Contact', backref='author', lazy='dynamic')

#     def __init__(self, email, password, image, name, uuid):
#         self.email = email
#         self.name = name
#         self.password = password
#         self.image = image
#         self.name = name 
#         self.uuid = uuid

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)




# class Task(db.Model):
#     __tablename__ = 'task'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     priority = db.Column(db.String)
#     status = db.Column(db.String)
#     item_type = db.Column(db.String)
#     category = db.Column(db.String)
#     task_note = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
#     def __init__(self, title, priority, status, item_type, category, task_note, author):
#         self.title = title
#         self.priority = priority
#         self.status = status
#         self.item_type = item_type
#         self.category = category
#         self.task_note = task_note
#         self.author = author

#     def __repr__(self):
#         return f'<Tasks {self.title}>'


# class Contact(db.Model):
#     __tablename__ = 'contact'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)    
#     name = db.Column(db.String)
#     telephone = db.Column(db.String)
#     email = db.Column(db.String)
#     image = db.Column(db.String)
#     company = db.Column(db.String)
#     category = db.Column(db.String)
#     contact_type = db.Column(db.String)
#     title = db.Column(db.String)
#     notes = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __init__(self, name, telephone, email, image, company, contact_type, category, title,  notes):
#         self.name = name
#         self.telephone = telephone
#         self.email = email
#         self.image = image
#         self.company = company
#         self.contact_type = contact_type
#         self.category = category
#         self.title = title
#         self.notes = notes
    
#     def __repr__(self):
#         return f'<Contacts {self.name}>'


