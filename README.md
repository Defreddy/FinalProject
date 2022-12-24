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
- [x] 1 API in GitHub Repostiory: <a href="https://github.com/Defreddy/Basicproject_frederikcrauwels" target="_blank">Take a look at THIS repo (the one you are currently viewing...)</a>.
- [x] 1 Front-end in GitHub repository: <a href="https://github.com/Defreddy/Defreddy.github.io" target="_blank">Github.io pages setup (is not fully functioning - POST requests do not work with GitHub pages</a>.
- [x] Description of the chosen theme, API, Front-end and link(s) + README.md customization.
- [x] Postman requests of API + screenshots README.md.
- [x] OpenAPI Docs screenhots README.md.

### REST API

- [x] At least 2 GET Endpoints (4 provided).
- [x] At least 1 POST endpoint (1 provided).
- [x] Validations.
- [x] Usage of path parameters, query parameters and body.

### DEPLOYING

- [x] API Docker container automation via GitHub Actions (2x provided for DB and API image).
- [x] API Docker container deployment via Okteto Cloud and Docker Compose.

### FRONT-END

- [x] Simple front-end, based on AlpineJS -> This has been changed to python:3.11.0-slim.
- [x] Deployment of front-end.

### ADDITIONAL FACTORS

- [x] Front-end styling (CCS - BootStrap Theme).
- [x] API interaction with Database (MySQL).
- [x] Additional inspiration... (PHPMyAdmin, .env file inside API container including GitHub secrets, CORS and additional GET requests, DB automation deployment with init.sql and .csv input file).


## Chosen Theme

The theme has been chosen based upon CVEs and vulnerabilities. A CVE are [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures). The list has been provided by CISA, documenting [known and actively exploited vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

## Usage and links

```bash
# Clone this repository or simply open via GitHub Desktop!
$ git clone https://github.com/Defreddy/Basicproject.git

# Go into the repository
$ cd Basicproject

# Make sure to launch Docker Desktop and simply run
$ docker compose up

# A variety of links can be accessed including the following:
$ localhost:8051  | This is your API website / Alpine / Slim.
$ localhost:8082  | This is your PHPMyAdmin - which will provide a much easier way of working with the MySQL DB. 
$ index.html      | You can simply open up the index.html locally to get a localhost view on your API calls!
                  | You can access this file in the Website folder.
```

> **Note**
> Certain URLs / parameters in this project need to be adjusted accordingly. There is a website available with <localhost> parameters.
> You must adjust the CORS table (allow_origins=['*'] = easiest way) and the GitHub secrets will not work for basicproject.yml. You could still define your own .env file!

You can view a live version of the provided APIs:
* [Here you can view the live website on GitHub pages - POST is NOT working here](https://defreddy.github.io/)
* [Here you can view the live website on sinners webhosting - POST DOES WORK here](https://frederikcrauwels.sinners.be/)

On these webpages you can:
* [Obtain a CVE by its name (GET - cveName)](https://frederikcrauwels.sinners.be/#page-top)
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/searchCVE.png)

* [Create a new CVE with additional details (POST - createcve)](https://frederikcrauwels.sinners.be/#add)
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/newCVE.png)

* [Obtain a better view on a variety of CVEs based on product name (GET - ?query=PRODUCT NAME)](https://frederikcrauwels.sinners.be/#product)
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/Products.png)

* [View all available CVEs based on the provided data in the DB (GET - allcve)](https://frederikcrauwels.sinners.be/#list)
![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/allCVE.png)

You can view a live version of the provided API itself (server):
* [Okteto API deployment DOCS](https://api-service-defreddy.cloud.okteto.net/docs)

![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/FastAPI-DOCS.png)

You can view a live version of the provided PHPMyAdmin (server):
* [PHPMyAdmin](https://phpmyadmin-defreddy.cloud.okteto.net/)

![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/CVE-Details.png)

> **Note**
> GitHub pages has disabled the use of POST requests: [POST is not working here!](https://stackoverflow.com/questions/37761926/does-github-pages-allow-http-post-method)
> The MySQL server is also deployed in Okteto Cloud but cannot be accessed by URL.

## Postman Requests

Take a closer look at the DOCS provided: [Okteto API DOCS](https://api-service-defreddy.cloud.okteto.net/docs)

![screenshot](https://github.com/Defreddy/Basicproject_frederikcrauwels/blob/main/Pictures_Readme/FastAPI-DOCS.png)

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


## Additional requests

As the assignment is primarily focussed around API calls - additional points could be rewarded if additional factors were taken into consideration.

- [x] Front-end styling (CCS - BootStrap Theme) - personally customized according to the specifications of this assignment.
- [x] API interaction with Database (MySQL). DB IaC automation deployment with init.sql and .csv input file. The entire DB is build based on this assignment, including init.sql automation for a complete automatic experience based on a .CSV input file. Only adjust the CSV -> deploy automatically in every other way (do not adjust the name of the CSV file). This also includes CRUD, DATABASE, MODEL and SCHEMA.py files.
- [x] PHPMyAdmin in order to be able to fully utilize the DB from your browser / deployment. No need for additional software / installs. 
- [x] .env file inside API container including GitHub secrets - this part of the integration will make sure certain parameters are hidden from others.
- [x] Additioan GET requests (required 2, created 4).
- [x] CORS has been adjusted to be able to acces both GitHub pages and custom-hosted solution.
- [x] A complete IaC deployment thanks to multiple Dockerfiles, GitHub workflows / actions and docker-compose.yml



