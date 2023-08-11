from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    local = Column(String())
    
    pets = relationship("PetOwner", back_populates="owner")
    
    def __repr__(self):
        return f"<Owner(id={self.id}, name='{self.name}', local='{self.local}')>"

class Pet(Base):
    __tablename__ = 'pets'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
    owners = relationship("PetOwner", back_populates="pet")
    # games = relationship("PetGame", back_populates="pets")
    
    def __repr__(self):
        return f"<Pet(id={self.id}, name='{self.name}')>"

class PetOwner(Base):
    __tablename__ = 'pet_owners'
    
    id = Column(Integer(), primary_key=True)
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    
    owner = relationship("Owner", back_populates="pets")
    pet = relationship("Pet", back_populates="owners")
    
    def __repr__(self):
        return f"<PetOwner(id={self.id}, owner_id={self.owner_id}, pet_id={self.pet_id})>"

# class PetGame(Base):
#     __tablename__ = 'pet_game'
    
#     id = Column(Integer, primary_key=True)
#     pet_id = Column(Integer, ForeignKey('pet.id'), nullable=False)
#     game_name = Column(String, nullable=False)
    
#     pet = relationship("Pet", back_populates="pet_game")
    
#     def __repr__(self):
#         return f"<PetGame(id={self.id}, pet_id={self.pet_id}, game_name='{self.game_name}')>"
