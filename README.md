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
- [x] Deployment of API container(s) on Okteto Cloud via Dockere Compose.

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

## Postman Requests

![screenshot](https://github.com/Defreddy/FinalProject/blob/main/Pictures_Readme/Authentication.gif)

* [GET - cveID](https://api-service-defreddy.cloud.okteto.net/cve/1)
    - This API can call a parameter thanks to a personal ID. Adjust the last path parameter {cveID}.
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/GET1.png)

* [GET - cveName](https://api-service-defreddy.cloud.okteto.net/cveName/CVE-2020-5735)
    - This API can call a parameter thanks to a personal cve NAME (CVE-YEAR-ID). Adjust the last path parameter {cveName}.
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/GET2.png)

* [GET - ?query=PRODUCT NAME](https://api-service-defreddy.cloud.okteto.net/product/?query=FTA)
    - This API can call a parameter thanks to a product name. Adjust the last query parameter to ?query={Product}.
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/GET3.png)

* [GET - allcve](https://api-service-defreddy.cloud.okteto.net/cve/1)
    - This API can call every single CVE in the DB.
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/GET4.png)

* [POST - createcve](https://api-service-defreddy.cloud.okteto.net/createcve/)
    - This API can POST a new CVE with additional details. Adjust parameters through a BODY JSON (Beautify) input. The ID will adjust automatically.
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/POST1.png)




