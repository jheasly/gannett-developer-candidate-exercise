## How to run this locally

You'll need [Python 3](https://installpython3.com/mac/) and [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv) installed on your machine.  
You'll end up with a virtual environment containing a Django 3.1.3 project with just one app, `gcde`.

1. Copy the project onto your machine from GitHub.

1. From the command line of your terminal app, `cd` into the `gannett-developer` directory created when you copied the project to your machine. If you see a `Pipfile` you're in the right directory!

1. Then from the command line, do the following:
```
$ pipenv install
$ pipenv shell
$ cd django313
$ python manage.py migrate
$ python manage.py runserver
```
... and you should see something like:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 19, 2020 - 15:23:29
Django version 3.1.3, using settings 'django313.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
To view the feature set, point your local browser at http://127.0.0.1:8000/

## Tests
To run tests (from the same directory that you did `$ python manage.py runserver`):
```
$ python manage.py test gcde
```