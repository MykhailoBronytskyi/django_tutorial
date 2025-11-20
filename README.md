# [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)


### Part 1 - Getting Started (check)
### Part 2 - Applications and Routes (check)
### Part 3 - Templates (check)
### Part 4 - Admin page (check)
----------------

### Part 5 - Database and Migrations (TBD)
### Part 6 - User Registration (TBD)
### Part 7 - Login and Logout System (TBD)

### Commands

#### Install django
```
pip install django
python -m django --version
```
#### Create project and startserver
```
django-admin
django-admin startproject name
python manage.py runserver
```
* HTTP addresses:
    * http://127.0.0.1:8000/
    * http://localhost:8000/

#### Create app
```
python manage.py startapp name
```
* HTTP addresses:
    * http://127.0.0.1:8000/blog/
    * http://127.0.0.1:8000/blog/about/


#### Make migrations (to the DB)
```
python manage.py makemigrations
python manage.py migrate
```
#### Create admin (superuser)
```
python manage.py createsuperuser
```
<!-- Username (leave blank to use 'user'): Mykhailo -->
<!-- Email address: mukhailobronutskyi@gmail.com -->

<!-- TestUser -->
<!-- password: testing321 -->