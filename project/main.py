from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi_login import LoginManager
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi_login.exceptions import InvalidCredentialsException #Exception class
from fastapi.responses import RedirectResponse,HTMLResponse
from os import path

import auth
import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

SECRET = "5cb761c7d4f7bda95677a460ad3a9266800fb594516ac51428dddb6ea9310ea3"
manager = LoginManager(SECRET,token_url='/auth/login',use_cookie=True)
manager.cookie_name = "some-name"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "https://friendly-jelly-004ab4.netlify.app/",
    "https://api-service-deployment-defreddy.cloud.okteto.net/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

fake_db = {'string': {'password': 'string'}}

@manager.user_loader()
def load_user(email: str):  # could also be an asynchronous function
    user = fake_db.get(email)
    return user

@app.post("/auth/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    user = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data={"sub":username}
    )
    resp = RedirectResponse(url="/users/",status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp

@app.get("/private")
def getPrivateendpoint(_=Depends(manager)):
    return "You are an authentciated user"

pth = path.dirname(__file__)

@app.get("/",response_class=HTMLResponse)
def loginwithCreds(request:Request):
    with open(path.join(pth, "..\Website\login.html")) as f:
        return HTMLResponse(content=f.read())

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/userdata/", response_model=schemas.UserData)
def create_item_for_user(
    user_id: int, userData: schemas.userDataCreate, db: Session = Depends(get_db)):
    return crud.create_user_data(db=db, userData=userData, user_id=user_id)

@app.put("/users/{user_id}/userdata/", response_model=schemas.userDataUpdate)
def update_item_for_user(user_id: int, userData: schemas.userDataUpdate, db: Session = Depends(get_db)):
    return crud.update_user_data(db=db, userData=userData, user_id=user_id)

@app.delete("/users/{user_id}/userdata/", response_model=schemas.userDataRemove)
def remove_item_for_user(user_id: int, db: Session = Depends(get_db)):
    return crud.remove_user_data(db=db, user_id=user_id)

@app.get("/userdata/", response_model=list[schemas.UserData])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    userData = crud.get_userData(db, skip=skip, limit=limit)
    return userData

@app.get("/userme/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db,token)
    return current_user

@app.get("/gerechten/", response_model=list[schemas.Gerecht])
def read_gerechten(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gerecht = crud.get_gerechten(db, skip=skip, limit=limit)
    return gerecht

@app.post("/gerechten/", response_model=schemas.Gerecht)
def create_gerecht(gerecht: schemas.GerechtenCreate, db: Session = Depends(get_db)):
    db_gerechten = crud.get_gerecht_by_name(db, gerecht=gerecht.naamGerecht)
    if db_gerechten:
        raise HTTPException(status_code=400, detail="Dish already registered. Please rename the dish, or look at the menu provided.")
    return crud.create_gerecht(db=db, gerecht=gerecht)

@app.get("/ingredients/", response_model=list[schemas.Ingredient])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ingredient = crud.get_ingredients(db, skip=skip, limit=limit)
    return ingredient

@app.post("/ingredients/{idGerecht}", response_model=schemas.Ingredient)
def create_ingredients(idGerecht: int, ingredients: schemas.IngredientsCreate, db: Session = Depends(get_db)):
    db_gerechten = crud.get_ingredient_by_name(db, idGerecht=idGerecht, ingredients=ingredients.naamIngredient)
    if db_gerechten:
        raise HTTPException(status_code=400, detail="Ingredient already registered. Please take a look at the menu for the added ingredient name specifically.")
    return crud.create_ingredient(db=db, idGerecht=idGerecht, ingredients=ingredients)
