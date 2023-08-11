from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Owner, Pet, PetOwner
if __name__ == '__main__':
    engine = create_engine('sqlite:///pocket-companions.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Pet).delete()
    session.query(Owner).delete()
    session.query(PetOwner).delete()
    gomez = Pet(name="Gomez")
    gunnar = Owner(name="Gunnar",local= "Suburban")
    Anahi = Owner(name="Anahi",local= "Suburban")
    owner1 = PetOwner(owner = gunnar,  pet = gomez)
    session.add_all([gomez,gunnar, owner1, Anahi])
    session.commit()
