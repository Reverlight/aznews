# aznews

## How to install

* Install python 3
* Create virtualenv
* Git clone https://github.com/Reverlight/aznews_project.git
* ``pip install -r requirements``
* Add your PostGreSQL credentials in settings.py (databases) 
* Create credentials.py file in root folder. Provide SECRET_KEY_DJANGO and OPEN_WEATHER_MAP_API_KEY like following:

  SECRET_KEY_DJANGO = 'YOUR_DJANGO_KEY'

  OPEN_WEATHER_MAP_API_KEY = 'YOUR_API_KEY'


* LOOK FOR WEATHER API HERE:
https://openweathermap.org/appid

## Optional
* Add initial news: ``python manage.py loaddata aznews_app/fixtures/data.json``

## Warning
* PostGreSQL is required!

## Admin
* Create superuser:
  ``python manage.py createsuperuser``
* Visit url root + \admin. For example http://127.0.0.1:8000/admin/
* Enter User Credentials
* Now you can edit\add news and it's categories

## Previews
![Preview1](Preview1.png)
![Preview2](Preview2.png)
![Preview3](Preview3.png)

