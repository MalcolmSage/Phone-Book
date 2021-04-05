from peewee import PostgresqlDatabase, Model, CharField

db = PostgresqlDatabase('phonebook', user='postgres', password="myPassword", host='localhost', port=5432)

db.connect()
# Base
class BaseModel(Model):
    class Meta:
        database = db

# Person Model
class People(BaseModel):
    first_name = CharField()
    number = CharField()

db.create_tables([People], safe=True)

# People(first_name='Malcolm', number='555-777-3333').save()

def prompts_ask():
    selection = int(input("Return to the main menu? 1 = Yes or 2 = No: "))
    if selection == 1:
        prompts()
    elif selection == 2:
        print("Goodbye")
    else:
        prompts_ask()

def prompts():
    print("Please read the following text, as the options have been changed")
    print("Select 1 for a list of all your contacts")
    print("Select 2 for to search for a specific person")
    print("Select 3 to add a new contact")
    print("Select 4 to close this phonebook")
    selection = int(input("Please choose now: "))
    while selection < 1 or selection > 4:
        print("Invalid selection")
        selection = int(input("Please choose again: "))
    
    # List
    if selection == 1:
        print("All Contacts")
        people = People.select()
        for person in people:
            print(f'{person.first_name}, {person.number}')
        prompts_ask()

    # Searching
    elif selection == 2:
        print("Contact search")
        print("Who are you looking for?")
        search = input("First Name: ")
        continued = 1
        while People.select().where(People.first_name != search) and continued == 1: 
            continued = int(input("No {search} found. Would you like to search again? 1 = Yes or 2 = No: "))
            if continued == 2:
                prompts()
            elif continued == 1:
                search = input("First Name: ")
        if People.select().where(People.first_name == search):
            found = People.select().where(People.first_name == search)
            for person in found:
                print(f'{person.first_name}, {person.number}')

    # Create
    elif selection == 3:
        print("New Contact")
        add_first_name = input("First Name: ")
        add_number = input("Number: ")
        People(first_name=add_first_name, number=add_number).save()
        prompts_ask()


    else:
        print("Goodbye")
prompts()


    