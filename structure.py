import datetime

from peewee import *
db = MySQLDatabase('library', user='root', password='')


bookStatus = ( (1, "New") , (2, "Used") , (3, 'Damaged') )
# class BaseModel(Model):
#     class Meta:
#         database = db

class Author(Model):
    name = CharField()
    location = CharField(null=True)
    class Meta:
        database = db
class Publisher(Model):
    name = CharField(unique=True)
    location = CharField(null=True)

    class Meta:
        database = db

class Category(Model):
    name = CharField(unique=True)
    parent_category =CharField()

    class Meta:
        database = db

class Book(Model):
    title = CharField(unique=True)
    description = TextField(null=True)
    category = ForeignKeyField(Category, backref="category" , null=True)
    code = CharField(null=True)
    barcode = CharField()
    part_order = IntegerField(unique=True)
    publisher = ForeignKeyField(Publisher, backref="publisher",null=True)
    price = DecimalField()
    author = ForeignKeyField(Author, backref="author" ,null=True)
    branch = ForeignKeyField(Author, backref="branch", null=True)
    image = CharField(null=True)
    status = CharField(choices=bookStatus)
    date = DateTimeField()

    class Meta:
        database = db
class Client(Model):
    name = CharField(unique=True)
    mail = CharField(null=True, unique=True)
    phone =  CharField(null=True )
    date = DateTimeField(default=datetime.datetime.now())
    national_id = IntegerField(null=True,unique=True)

    class Meta:
        database = db

class Branch(Model):
    name = CharField()
    code = CharField()
    location = CharField()

    class Meta:
        database = db

class Employee(Model):
    name = CharField(unique=True)
    mail = CharField(null=True)
    phone = CharField()
    date = DateTimeField(default=datetime.datetime.now())
    national_id = IntegerField(unique=True)
    priority = IntegerField(unique=True)

    class Meta:
        database = db


processType = ((1, "Rent") , (2, "Retrieve"))

class Daily_Movements(Model):
    book = ForeignKeyField(Book, backref="daily_book")
    client = ForeignKeyField(Client, backref="book_client")
    type = CharField(choices=processType)
    date = DateTimeField(default=datetime.datetime.now())
    branch = ForeignKeyField(Branch, backref='Daily_branch')
    book_from = DateField()
    book_to  = DateField()
    employee = ForeignKeyField(Employee, backref='Daily_employee')

    class Meta:
        database = db

actionType = ((1,'Login') ,(2, "Create"), (3, "Update") ,(4, "Delete") )

tableChoices = ((1,'Book') ,(2, "Client"), (3, "Employee") ,(4, "Category") , (5, "Branch")  , (6, "Daily Movements") , (7, "Publisher") , (8, "Author"))
class History(Model):
    employee = ForeignKeyField(Employee, backref='history_employee')
    action = CharField(choices=actionType)
    table = CharField(choices=tableChoices)
    date = DateTimeField(default=datetime.datetime.now())
    branch = ForeignKeyField(Employee, backref='history_branch')

    class Meta:
        database = db


db.connect()
db.create_tables([Category,Book,Client,Branch,Publisher,Author,Employee,Daily_Movements, History,])