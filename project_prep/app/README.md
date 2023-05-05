# README

Flask App

app.init.py

```py
from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
```

app.config.py

```py
import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Create Python .gitignore

```bash
curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
```

Install dependencies

```bash
pipenv install flask flask-sqlalchemy alembic flask-migrate python-dotenv sqlalchemy wtforms flask-wtf
```

Install dev dependencies

```bash
pipenv install --dev pylint pycodestyle rope pytest
```

Start Python environment

```bash
pipenv shell
```

.flaskenv

```code
FLASK_APP=app
```

.env

```code
FLASK_DEBUG=1
SECRET_KEY=«some random bytes»
DATABASE_URL=sqlite:///dev.db
```

Generate random string

```bash
openssl rand -base64 12
```

Sample File Structure

```code
.
├── .env
├── .flaskenv
├── app
│   ├── __init__.py
│   ├── config.py
│   └── routes
│       └── __init__.py
└── models
       └── __init__.py
     
```

