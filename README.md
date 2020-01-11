# Setup
1. clone this repo
1. `docker-compose up -d`
1. `./init_script.sh` this will:
    * initialize the django database
    * create a django superuser
    * insert some demo data
1. navigate your browser to http://localhost:8000
1. *optional:* log into the backend at http://localhost:8000/admin/ with the account created by the init script


## Assumptions:
* docker engine 1.13.0+ & docker-compose are installed and `docker-compose` can be executed by the current user
* curl is installed
* enough drive space for the docker containers