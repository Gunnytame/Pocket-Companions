from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Owner, Pet, PetOwner

engine = create_engine('sqlite:///pocket-companions.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_owner():
    try:
        owner_dict = {
            'name': input("Enter owner's name: "),
            'local': input("Enter owner's local: ")
        }
        
        owner = Owner(**owner_dict)
        session.add(owner)
        session.commit()
        print("Owner added successfully!")
    
    except Exception as e:
        print("An error occurred:", e)

def add_pet():
    name = input("Enter pet's name: ")
    pet = Pet(name=name)
    session.add(pet)
    session.commit()
    print("Pet added successfully!")

def link_pet_owner():
    owner_id = int(input("Enter owner's ID: "))
    pet_id = int(input("Enter pet's ID: "))
    
    owner = session.query(Owner).get(owner_id)
    pet = session.query(Pet).get(pet_id)
    
    if owner and pet:
        pet_owner = PetOwner(owner=owner, pet=pet)
        session.add(pet_owner)
        session.commit()
        print("Pet linked to owner successfully!")
    else:
        print("Owner or pet not found.")

def main():
    while True:
        print("\n1. Add Owner\n2. Add Pet\n3. Link Pet to Owner\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            add_owner()
        elif choice == '2':
            add_pet()
        elif choice == '3':
            link_pet_owner()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

session.close()

