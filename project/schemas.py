from pydantic import BaseModel
from typing import Optional


class userDataBase(BaseModel):
    naam: str
    leeftijd: int
    niveauKoken: str 
    favorieteKeuken: str 


class userDataCreate(userDataBase):
    pass

class userDataRemove(userDataBase):
    naam: str | None = None
    leeftijd: int | None = None
    niveauKoken: str | None = None
    favorieteKeuken: str | None = None


class UserData(userDataBase):
    userID: int
    
    class Config:
        orm_mode = True

class userDataUpdate(userDataBase):
    naam: str | None = None
    leeftijd: int | None = None
    niveauKoken: str | None = None
    favorieteKeuken: str | None = None

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    userInfo: list[UserData] = []

    class Config:
        orm_mode = True

class Gerechten(BaseModel):
    naamGerecht: str
    recept: str
    keukenType: str

class GerechtenCreate(Gerechten):
    pass

class Ingredients(BaseModel):
    naamIngredient: str
    hoeveelheidIngredient: str

class IngredientsCreate(Ingredients):
    pass

class Ingredient(Ingredients):
    idIngredient: int
    idGerecht: int
    
    class Config:
        orm_mode = True

class Gerecht(Gerechten):
    idGerecht: int
    ingredientInfo: list[Ingredient] = []
    
    class Config:
        orm_mode = True