# This is a Python project

## Some Phyton commands:
* To run project in local `python3 manage.py runserver`

## To Make DataBase by Models
* Cretate models in the models files.
* Create migrations: `python3 manage.py makemigrations`
* Run the migration that just was created `python3 manage.py sqlmigrate miapp 0001`
* Run the migration: `python3 manage.py migrate`

## To reconfigurate a sercret key
It is possible you need to configure (SECRET_KEY) value into settings.py file aim to protect this value at github. [To achieve it click here.](https://stackoverflow.com/questions/64208678/hiding-secret-key-in-django-project-on-github-after-uploading-project) 

In case you need to create a new (SECRET_KEY). [Click here](https://tech.serhatteker.com/post/2020-01/django-create-secret-key/)
