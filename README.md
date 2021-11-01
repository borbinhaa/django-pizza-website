# About it
Thats a simple website for a pizza seller, I made it to learn, that was my first experience making
a website all by myself.

### How to use it

- Install git:

```
git clone https://github.com/borbinhaa/django-pizza-website.git .
```

- **Windows**:

```
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-crispy-forms pillow
python manage.py migrate
python manage.py runserver
```


- **Linux**:

```
python3.7 -m venv venv
. venv/bin/activate
pip install django django-crispy-forms pillow
python manage.py migrate
python manage.py runserver
```

- **Mac**

```
python -m venv venv
. venv/bin/activate
pip install django django-crispy-forms pillow
python manage.py migrate
python manage.py runserver
```

- Now some parts of the website you need to complete, It is necessary to do the flavors and add the stores address. To do that:

```
python manage.py createsuperuser
http://127.0.0.1:8000/admin/
```

Hope you enjoy!
