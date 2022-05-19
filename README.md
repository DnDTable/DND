# 🎲 DND-Table 

# Introduction 
> This project aims to make it easier for players to have D&D gaming sessions. It includes a number of features necessary to ensure the comfort of both players and presenters. \
In our project, the function of registering new users is implemented. There is also an encyclopedia containing basic information from the D&D licensing rules. \
The main function of our project is the game table, which facilitates the visualization of some game moments. There are also a number of special features that simplify the gameplay. Among these functions are the generation of game dice rolls, character sheets, calculation by formulas.

# 🛠 Requirements
  [Python 3.10.x](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe) \
  [Django](https://www.djangoproject.com/) 
  
  ### Python Libs:
  - Django : 4.0.4
  - Django-environ : 0.8.1
  - Psycopg2-binary : 2.9.3

  [Docker](https://www.docker.com/get-started/) \
  [PostgreSQL](https://hub.docker.com/_/postgres) 

  [NodeJs](https://nodejs.org/en/)
  
 # How to run
  1. Run Docker-Compose file: <code> $ docker-compose up </code>
  2. Make Django db migrations: <code> $ python manage.py migrate</code>
  3. Run Django server: <code>python manage.py runserver</code>
