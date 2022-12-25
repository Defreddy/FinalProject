from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    userInfo = relationship("userData", back_populates="owner")


class userData(Base):
    __tablename__ = "userData"

    userID = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    naam = Column(String)
    leeftijd = Column(Integer)
    niveauKoken = Column(String)
    favorieteKeuken = Column(Integer)

    owner = relationship("User", back_populates="userInfo")

class Gerechten(Base):
    __tablename__ = "gerechten"

    idGerecht = Column(Integer, primary_key=True, index=True)
    naamGerecht = Column(String)
    recept = Column(String)
    keukenType = Column(String)

    ingredientInfo = relationship("Ingredients", back_populates="allIngredients")

class Ingredients(Base):
    __tablename__ = "ingredients"

    idIngredient = Column(Integer, primary_key=True, index=True)
    naamIngredient = Column(String)
    hoeveelheidIngredient = Column(String)
    idGerecht = Column(Integer, ForeignKey("gerechten.idGerecht"), index=True)

    allIngredients = relationship("Gerechten", back_populates="ingredientInfo")

