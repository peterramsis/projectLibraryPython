from peewee import *
db = MySQLDatabase('library', user='root', password='')

# class BaseModel(Model):
#     class Meta:
#         database = db

class Author(Model):
    pass
class Publisher(Model):
    pass

class Category(Model):
    name = CharField()
class Book(Model):
    title = CharField()
    description = TextField()
    category = ForeignKeyField(Category, backref="category")
    code = CharField()
    publisher = ForeignKeyField(Publisher, backref="publisher")
    price = DecimalField()
    author = ForeignKeyField(Author, backref="author")
    image = CharField()
    status = CharField()
    date = DateTimeField()
class Client(Model):
    name = CharField()
    mail = CharField()
    phone =  CharField()
    date = DateTimeField()
    national_id = IntegerField()
class Branch(Model):
    name = CharField()
    code = CharField()
    location =CharField()

class Employee(Model):
    name = CharField()
    mail = CharField()
    phone = CharField()
    date = DateTimeField()
    national_id = IntegerField()
    permission = IntegerField()

class Daily_Movements(Model):
    book = ForeignKeyField(Book, backref="daily_book")
    client = ForeignKeyField(Client, backref="book_client")
    type = CharField()
    date = DateTimeField()
    branch = ForeignKeyField(Branch, backref='Daily_branch')
    book_from = DateField()
    book_to  = DateField()
    employee = ForeignKeyField(Employee, backref='Daily_employee')

class History(Model):
    employee = ForeignKeyField(Employee, backref='history_employee')
    action = CharField()
    table = CharField()
    date = DateTimeField()
    branch = ForeignKeyField(Employee, backref='history_branch')


db.connect()
db.create_tables([Book,Client,Branch,Publisher,Author,Category,Employee])