HCIProject
==========

In class project for HCI course


###Dev
####set up
1. Install Python 2.7 and pip
2. ```pip install -r requirements.txt```
3. ```python manage.py migrate```
4. To use local settings:  
  * create hciproject/settings_dev.py
  * put anything here. For example:
    ```

    DEBUG = True  
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3'),
    }
  }

    ```

####Run
```
python manage.py runserver
```
