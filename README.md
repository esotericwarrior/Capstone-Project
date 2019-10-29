# Capstone-Project
OSU CS467 Online Capstone Project

Collaborators
-------------
Kristen Harrison

Tristan Santiago

Alexis Tucker



### Project Structure ###


| Location                                  |  Content                                           |
|-------------------------------------------|---------------------------------------------------|
| `/backend/Capstone`                       | Django REST Project & Backend Config              |
| `/backend/venv`                           | Python Virtual Environment                        |
| `/backend/Capstone/templates/index.html`  | Django App Entry Point                            |
| `/frontend`                               | Vue App                                           |
| `frontend/src/main.js`                    | JS Application Entry Point                        |
| `/public/index.html`                      | Html Application Entry Point (`/`)                |
| `/public/static`                          | Static Assets                                     |
| `/dist/`                                  | Bundled Assets Output (generated at `yarn build`) |

### Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pip - [instructions](https://pypi.org/project/pip/)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

## Setup Template

```
$ git clone https://github.com/esotericwarrior/Capstone-Project.git
$ cd Capstone-Project
```

Setup
```
$ yarn install
$ pipenv install --dev && pipenv shell
$ source venv/Scripts/activate (from within `/backend/venv`)
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```

From another tab in the same directory:

```
$ yarn serve
```

The Vue application will be served from [`localhost:8080`](http://localhost:8080/) and the Django API
and static files will be served from [`localhost:8000`](http://localhost:8000/).

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in [`vue.config.js`](/vue.config.js) is used to route the requests
back to django's API on port 8000.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```
