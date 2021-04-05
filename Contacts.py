from peewee import PostgresqlDatabase, Model, CharField

db = PostgresqlDatabase('phonebook', user='postgres', password="myPassword", host='localhost', port=5432)

db.connect()
# Base
class BaseModel(Model):
    class Meta:
        database = db

# Person Model
class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    number = CharField()


# db.drop_tables([Person])
db.create_tables([Person], safe=True)

# Person(first_name='Malcolm', last_name='Sage', number='555-777-3333').save()

