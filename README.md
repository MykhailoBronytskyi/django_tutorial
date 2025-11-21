# [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)


### Part 1 - Getting Started (check)
### Part 2 - Applications and Routes (check)
### Part 3 - Templates (check)
### Part 4 - Admin page (check)
### Part 5 - Database and Migrations (TBD)

----------------

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
python manage.py makemigrations # prepare changes
python manage.py migrate # commit changes
```
#### Create admin (superuser)
```
python manage.py createsuperuser
```
<!-- Username (leave blank to use 'user'): Mykhailo -->
<!-- Email address: mukhailobronutskyi@gmail.com -->

<!-- TestUser -->
<!-- password: testing321 -->

python manage.py makemigrations
python manage.py sqlmigrate blog 0001
python manage.py migrate

django python shell:
python manage.py shell -i python

from blog.models import Post
from django.contrib.auth.models import User

User.objects.all()
User.objects.first()
User.objects.filter(username='TestUser')
User.objects.filter(username='TestUser').first()

user = User.objects.filter(username='TestUser').first()
user
user.id
user.pk

user = User.objects.get(id =1)
user

Post.objects.all()
post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
Post.objects.all()

post_1.save()
Post.objects.all()

post_2 = Post(title='Blog 2', content='Second Post Content!', author_id=user.id)
post_2.save()
Post.objects.all()

post = Post.objects.first()
post.content
post.date_posted
post.author
post.author.email

user
user.post_set
user.post_set.all()
user.post_set.create(title='Blog 3', content='Third Post Content!')
Post.objects.all()
