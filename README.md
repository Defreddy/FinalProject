<h1 align="center">
  <br>
  <a href="https://media.giphy.com/media/l4Jz3a8jO92crUlWM/giphy.gif"><img src="https://media.giphy.com/media/l4Jz3a8jO92crUlWM/giphy.gif" alt="Snaky"></a>
  <br>
  IaC deployment with API integrations
  <br>
</h1>

<h4 align="center">An API and IaC integration with FastAPI.</h4>

<p align="center">
    API Deployment:
  <a href="https://hub.docker.com/repository/docker/freds00n/finalproject" target="_blank">
    <img src="https://img.shields.io/docker/automated/freds00n/basicproject?style=for-the-badge"
         alt="API">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#additional-requirements">Additional requirements</a> •
  <a href="#chosen-theme">Chosen Theme</a> •
  <a href="#usage-and-links">Usage and links</a> •
  <a href="#postman-requests">Postman Requests</a> •
  <a href="#hashing-and-SQLite-details">Hashing / SQLite details</a> •
  <a href="#front-end-details">Front-end details</a> •
  
  
</p>

![screenshot](https://github.com/Defreddy/finalproject/blob/main/Pictures_Readme/website.png)

## Key Features

### General requirements
- [x] Atleast 3 GET, 1 POST, 1 PUT and 1 DELETE endpoints: 6 GET, 5 POST, 1 PUT, 1 DELETE.
- [x] Atleast 3 entities via SQLite DB: 4 entities (Users, UserData, Ingredients and Gerechten).
- [x] Atleast hashing and 0Auth implemented.
- [x] Description of chose theme, API(s), extensions and link to GitHub README.md.
- [x] Postman requests displaying working functionality of APIs.
- [x] OpenAPI documentation.
- [x] Docker container for API deployment, automatically being pushed via Github Actions.
- [x] Deployment of API container(s) on Okteto Cloud via Docker Compose.

### Additional requirements

#### Security
- [x] Second version of the original API with Okta Auth0.
- [x] KrakenD gateway protecting APIs. 

> **Note**
> While i did try to implement the security features - i believe they will not be marked for the full grades, if marked at all.
> Okta Auth0 vs OpenID Connect is quite unclear for me, but i did link Auth0 to the application instead of using our own, custom generated tokens.
> KrakenD gateway can check one end-point by feeding it Auth0 credentials, as well as obtain valid tokens. The JWT validator is returning 401's thus not working as intended.

#### Front-end
- [ ] Front-end application for all GET and POST endpoints.
  - [x] Front-end hosting on Netlify.
  - [x] Front-end style additions (Bootstrap theme).
 
> **Note**
> Front-end application for all GET and POST endpoints is not marked as "completed", because not ALL GET and POST endpoints have been added.
> The reason is simple: authentication without a proper Javascript Framework is near-impossible. 
> I tried implementing fastapi-login to achieve the same for a simple HTML deployment, but is not possible for the current deployment and intended result. More information can be found at the bottom of this README -> Front-end details.

Added endpoints:
  - GET + POST gerechten.
  - GET + POST ingredients. Since the ingredients are included (via a relationship) in the "gerechten" request, this is not separatly added, except for the POST.
  - GET user data.

- All others are either (not added endpoints): 
  - POST, GET, DELETE, PUT, /me users: registering LOGIN users (which is simply not possible without proper Authorization / Javascript framework knowledge).
  - POST user data: the GET request has been provided - but for adding user data i believe this is not what any other user, but the user himself, should be able to do. This is also an Authorization request (for this simple reason: nobody should add or change user data, except for the user itself).

## Chosen Theme

Hello there, head chef! Hopefully your meals are deliciously seasoned (see meme at the top) because this project is fully seasoned for completion.
The chosen theme revolves around delicious recipes and ingredients as i love cooking myself! 
As this is a course assignment, a variety of general requirements need to be met.


## Usage and links

```bash
# Clone this repository or simply open via GitHub Desktop!
$ git clone https://github.com/Defreddy/FinalProject

# Go into the repository
$ cd FinalProject

# Make sure to launch Docker Desktop and simply run
$ docker compose up

# A variety of links can be accessed including the following:
$ localhost:8051  | This is your API website / Alpine / Slim. 

# Take a look at the API docs:
$ localhost:8051/docs
```

> **Note**
> The webserver has a built-in SQLite database and an attached volume so your data is persistent.
> Because the assignment requested a local SQLite DB + API server in one, there is unfortunately not an Okteto Cloud link available.

## Hashing and SQLite details

* ***Hashing***
  - Hashing is provided via Bcrypt and Argon2 protocols. As you can see in the image below, the user password is fully hashed.
  - In further examples you can learn more about authentication and how these hashed passwords work for users / authentication.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Hashing.png)

* ***SQLite database***
  - The application is supported by a SQLite database which comes with a volume. This will make sure data is persistent + API calls will interact with the database.
  - This is the reason i REMOVED the volume, and only utilized the api-service container itself, without a persistent volume specifically.
  - This means: once the application is restarted (Okteto = reboot), all previous data is removed, except for the one already included in the original deployment (bare minimum).

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Databasestructure.png)

## Postman Requests

Overview of the OpenAPI documentation which will be further highlighted below:

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/FastAPIDocs.png)

* ***Okteto Cloud***
  - As the deployment has two "services" - one main, one SQLlite / volume, the Okteto Cloud deployment is unable to create a single deployment.
Therefore a link towards a working production environment in the cloud is not possible.
  - It is advised to use a local git clone, or utilize the readily available docker image provided at the top of this readme.

With data volume (StatefulSet with TWO pods / deployments -> this is the reason this is a StatefulSet. Volume + Local API service in one deployment = StatefulSet):

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/OktetoCloud.png)

Without data volume (= clearly a deployment, thus obtains a proper Edpoint):

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/OktetoCloudCorrect.png)


* ***Authentication + GET - Users***
  - Below you can see how authentication is provided within the application. A couple of "locked" requests have been provided - but every single one should do exactly the same. Once you have the token, you are able to use the API. This example will show you how authentication can lock you out unless you have valid credentials.
  - Additionally you can notice how /users/ can be viewed as a working GET request. 

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Authentication.gif)

* ***POST - Creating Users***
  - In order to be able to access the application - you require a user. As the user "string" is being made by the default API call - you can create another one. 
  - This request is using a request body.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/createuser.gif)

* ***GET - user / me***
  - User / me is a self-check of the current user which can be utilized for further implementations (only the current user can change his user data, gerechten,...).
  - This API also required authentication - but will not be further dealt with. The current logged-in user is "String", which is also being displayed in the end.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/userme.gif)

* ***POST - Creating user data***
  - Since we now have working users for all authentication(s), it is time to add more details to our user: our name, age, cooking skill level and favorite kitchen.
  - This request is using a request body. This could be an example where User / Me could be further implemented to avoid having to provide a user_id, for example.
  - Since we have created a new user in the previous step (ID - 3), we will be using our newly created user!

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/createuserdata.gif)

* ***GET + DELETE + PUT - user data***
  - Dang it - i accidentally used my wrong pseudo-name and age. Time to change this data! We will review our user data and change it accordingly.
  - The other user accounts created some dummy data as well - which we will be removing in order to gain a better visibility for out PUT request.
  - As the "Delete" and "Put" could be implemented fairly similarly (copy-paste code...) for other parts i only provided them once, as an example.
  - GET: here we are able to view data.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/getuserdata.gif)

  - DELETE: here we can delete data solely based on user_id.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/deleteuserdata.gif)

  - PUT: here we can change any record from our user.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/putuserdata.gif)

* ***GET + POST gerechten***
  - Gerechten are "dishes" - since we are a 10-star head chef we will be sharing our dishes with the world!
  - POST: here we can delete data solely based on user_id.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/postgerecht.gif)

  - GET: here we are able to view data.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/getgerecht.gif)

* ***GET + POST ingredients***
  - A dish is not complete without ingredients... Which is what we will be adding here. Last but not least we will display the changed GET gerechten page, displaying ingredients.
  - POST ingredients: here we can add data.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/postingredient.gif)

  - GET ingredients: here we are able to view data.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/getingredient.gif)

  - GET Gerechten: here we are able to view data (ingredients being added). This will create one view / API with multiple tables: Gerechten and Ingredients combined!

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/getgerechtfinal.gif)

## Front-end details

The front-end part of this API integration is fully integrated with an Okteto Cloud deployment, and a Netlify hosting solution.
Details about Okteto Cloud have been fully discussed in a previous chapter.

### Netlify

Netlify is a hosting solution with automated GitHub deployment integrations. This allows you to host a GitHub .html website and automatically deploy new .html changes to your Netlify endpoint. This way, after each deployment, the code is automatically adjusted in your endpoint. Very handy!

The website URL: https://friendly-jelly-004ab4.netlify.app/index.html

Overview of such deployments:

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Netlify.png)

Here you can clearly see it distinguishes .HTML and any other changes. Each change that is NOT .html related, or linked to the /Website directory will be ignored and instantly "Canceled". If the change is happening within the /Website directory, the change will be put through to Netlify resulting in a Non-Canceled, or Published state.

The reason for this type of deployment is the settings. Simply point to the correct directory and you are ready to go, ignoring all other deployments that don't matter to your .HTML (or JS Framework) front-end. Also active "Active Builds" for continuous deployments:

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Netlify-details.png)

### API requests included in the front-end

As explained before - not all endpoints have been included for the simple reason of authentication not working as intended. 
Nonetheless, from a database perspective, 3 out of 4 entities are being displayed and included in this front-end.

You will be able to find more details about the front-end and back-end endpoint deployments in the following titles.

#### GET + POST gerechten / ingredients

The POST gerechten / dishes is simply being put at the top of the webpage. A production example can be seen below.
In this example you can clearly view when your request has been accepted or declined.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/RegisterDish.gif)

Once you have submitted a new dish, you can find the dish in the Menu section (once the webpage is refreshed):

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/DishDetails.png)

A "complicated" set of HTML coding and AlpineJS allows us to pull multiple data elements from one, big query.
This query includes your dish details AND your ingredientInfo - your ingredients. Those ingredients can also be added via the front-end.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/bigQuery.png)

This nifty piege of code will make sure a variety of aspects are instantly changing continuously:
  - FIRST DIV: this will retrieve all the information listed above in the query: naamGerecht, recept, keukenType, idGerecht and ingredientInfo with naamIngredient and hoeveelheidIngredient.
  - x-for EACH DISH: you will get a completely new, visual element. One single <DIV> element for dish. AlpineJS and HTML wizardry in one!
  - IMG: Since a variety of custom images have been provided (6 to be precise), the code will automatically change the picture according to the idGerecht, ID number.
  - Array within Array: this piece of code will also retrieve data from within the array "IngredientInfo". Double the x-for fun! This is the single reason why i don't need to do a GET Ingredients!

Not to mention, this small piece of HTML coding does a LOT of things.
```html
<div
x-cloak
x-data="{dishes: [], 'isLoading': true}"
x-init="fetch('https://api-service-deployment-defreddy.cloud.okteto.net/gerechten/')
.then(response => response.json())
.then(response => { dishes = response; isLoading = false; console.log(response); })"
>
<h1 x-show="isLoading">Loading...</h1>      
    <template x-for="dish in dishes" :key="dish.idGerecht">
        <div class="col-lg-4-center menu-item">
            <img :src="'assets/img/menu/menu-item-' + dish.idGerecht + '.png'" class="menu-img img-fluid" alt="">
            <h4 x-text="'Dish name: ' + dish.naamGerecht + ', Dish ID: ' + dish.idGerecht">></h4>
            <p class="ingredients" >Ingredients: </p>
            <template x-for="ingredient in dish.ingredientInfo">
                <p x-text="ingredient.hoeveelheidIngredient + ', ' +  ingredient.naamIngredient"></p>
            </template>
            <p class="ingredients" >Recipe: <span x-text="dish.recept"></span></p>
            <p class="price" x-text="'Dish culture: ' + dish.keukenType">
            </p>
          </div><!-- Menu Item -->
    </template>
</div>
```

Accompanied by relationships - you can obtain an array within an array:
```python
models.py:

class Gerechten(Base):
    __tablename__ = "gerechten"

    <elements>

    ingredientInfo = relationship("Ingredients", back_populates="allIngredients")

class Ingredients(Base):
    __tablename__ = "ingredients"

    <elements>

    allIngredients = relationship("Gerechten", back_populates="ingredientInfo")

schemas.py:

class Gerecht(Gerechten):
    idGerecht: int
    ingredientInfo: list[Ingredient] = []
    
    class Config:
        orm_mode = True
```

#### GET - user data

As adding (your own) user data is deemed as a privileged right - and without authorization / authentication - i simply cannot allow this.
Displaying the data on the other hand is not an issue at all.

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/GETuserdata.png)

Beneath you can see the code - and why the PREVIOUS GET request (Gerechten) is far more superior.
For each chef you need to copy-paste this exact, same code. While the gerechten code does all of this in one, single go... AND creates each element separately.
The code below has to be created for each chef / element, making your HTML file clumsy while you could do exactly the same as with gerechten / dishes (x-for wizardy).
```html
<div class="row gy-4">
  <div class="col-lg-4 col-md-6 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
    <div class="chef-member">
      <div class="member-img">
        <img src="assets/img/chefs/chefs-1.jpg" class="img-fluid" alt="">
        <div class="social">
          <a href=""><i class="bi bi-twitter"></i></a>
          <a href=""><i class="bi bi-facebook"></i></a>
          <a href=""><i class="bi bi-instagram"></i></a>
          <a href=""><i class="bi bi-linkedin"></i></a>
        </div>
      </div>
      <div class="member-info">
        <h4 x-text="chefList[0].naam"></h4>
        <span x-text="chefList[0].niveauKoken"></span>
        <p>Age: <span x-text="chefList[0].leeftijd"></span>
            Favorite kitchen: <span x-text="chefList[0].favorieteKeuken"></span></p>
      </div>
    </div>
  </div><!-- End Chefs Member -->
```

> **Note**
> This was obviously being done on purpose to display how much more thought and detail went into one advanced process, while the GET user data process is only a simple implementation. The GET gerechten / ingredients is clearly far more advanced and thought through.

#### POST ingredients