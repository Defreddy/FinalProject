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
  <a href="#chosen-theme">Chosen Theme</a> •
  <a href="#usage-and-links">Usage and links</a> •
  <a href="#postman-requests">Postman Requests</a> •
  <a href="#additional-requests">Additional requests</a>
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


* ***Hashing***
  - Hashing is provided via Bcrypt and Argon2 protocols. As you can see in the image below, the user password is fully hashed.
  - In further examples you can learn more about authentication and how these hashed passwords work for users / authentication.
![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/hashing.png)

* ***SQLite database***
  - The application is supported by a SQLite database which comes with a volume. This will make sure data is persistent + API calls will interact with the database.
![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/hashing.png)

## Postman Requests

Overview of the OpenAPI documentation which will be further highlighted below:
![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Databasestructure.png)

* ***Okteto Cloud***
  - As the deployment has two "services" - one main, one SQLlite / volume, the Okteto Cloud deployment is unable to create a single deployment.
Therefore a link towards a working production environment in the cloud is not possible.
  - It is advised to use a local git clone, or utilize the readily available docker image provided at the top of this readme.
![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/OktetoCloud.png)

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

  - GET Gerechten: here we are able to view data (ingredients being added).
![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/getgerechtfinal.gif)

