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

def prompts():
    print("Please read the following text, as the options have been changed")
    print("Select 1 for a list of all your contacts")
    print("Select 2 for to search for a specific person")
    print("Select 3 to add a new friend")
    print("Select 4 to close this phonebook")
    selection = int(input("Please choose now: "))
    while selection < 1 or selection > 4:
        print("Invalid selection")
        selection = int(input("Please choose again: "))
    if selection == 1:
        print("All Contacts")
    elif selection == 2:
        print("Contact search")
    elif selection == 3:
        print("New friend")
    else:
        print("Goodbye")
prompts()


    