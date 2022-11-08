from database import db


class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(100))
    date = db.Column("date", db.String(50))
    manager_id = db.Column("manager_id", db.Integer)

    def __init__(self, id, title, text, date, manager_id):
        self.id = id
        self.task_name = title
        self.content_text = text
        self.date_created = date
        self.date_due = manager_id


class Task(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    task_name = db.Column("task_name", db.String(300))
    content_text = db.Column("content_text", db.String(4000))
    date_created = db.Column("date_created", db.String(50))
    date_due = db.Column("date_due", db.String(50))
    assigned_id = db.Column("assigned_id", db.Integer)

    def __init__(self, id, task_name, content_text, date_created, date_due, assigned_id):
        self.id = id
        self.task_name = task_name
        self.content_text = content_text
        self.date_created = date_created
        self.date_due = date_due
        self.assigned_id = assigned_id


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    fname = db.Column("fname", db.String(50))
    lname = db.Column("lname", db.String(50))
    username = db.Column("username", db.String(50))
    password = db.Column("password", db.String(50))

    def __init__(self, id, fname, lname, username, password):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password