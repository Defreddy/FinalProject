from sqlalchemy.orm import Session
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import models
import schemas
import auth

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_userData(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.userData).offset(skip).limit(limit).all()

def create_user_data(db: Session, userData: schemas.userDataCreate, user_id: int):
    db_userData = models.userData(**userData.dict(), userID=user_id)
    db.add(db_userData)
    db.commit()
    db.refresh(db_userData)
    return db_userData

def update_user_data(db: Session, userData: schemas.userDataUpdate, user_id: int):
    find_user = db.query(models.userData).filter(models.userData.userID == user_id)
    get_first = find_user.first()
    data = userData.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(userData, key, value)
    find_user.filter(models.userData.userID == user_id).update(data, synchronize_session=False)
    db.commit()
    db.refresh(get_first)
    json_data = jsonable_encoder(get_first)
    return JSONResponse(content=json_data)

def remove_user_data(db: Session, user_id: int):
    find_user = db.query(models.userData).filter(models.userData.userID == user_id)
    find_user.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content="ok boomer")

def get_userPass(db: Session, query: str):
    products = db.query(models.User).filter(models.User.id.contains(query)).all()
    listProducts = []
    for prod in products:
        listProducts.append(prod)
    return listProducts

def get_gerechten(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gerechten).offset(skip).limit(limit).all()

def get_gerecht(db: Session, idGerecht: int):
    return db.query(models.Gerechten).filter(models.Gerechten.idGerecht == idGerecht).first()

def create_gerecht(db: Session, gerecht: schemas.GerechtenCreate):
    db_gerecht = models.Gerechten(naamGerecht=gerecht.naamGerecht, recept=gerecht.recept, keukenType=gerecht.keukenType)
    db.add(db_gerecht)
    db.commit()
    db.refresh(db_gerecht)
    return db_gerecht

def get_gerecht_by_name(db: Session, gerecht: str):
    return db.query(models.Gerechten).filter(models.Gerechten.naamGerecht == gerecht).first()

def get_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ingredients).offset(skip).limit(limit).all()

def create_ingredient(db: Session, ingredients: schemas.IngredientsCreate, idGerecht: int):
    db_ingredient = models.Ingredients(naamIngredient=ingredients.naamIngredient, hoeveelheidIngredient=ingredients.hoeveelheidIngredient, idGerecht=idGerecht)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def get_ingredient_by_name(db: Session, ingredients: str, idGerecht: int):
    return db.query(models.Ingredients).filter(models.Ingredients.idGerecht == idGerecht, models.Ingredients.naamIngredient == ingredients).first()
