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

Models

User

```py
from datetime import datetime
from ..dev import db


class User(db.Model):
    __tablename__ = "users"
    # Table Keys
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
```

Messages

```py
from datetime import datetime
from ..dev import db


class Message(db.Model):
    __tablename__ = "messages"
    # Table Keys
    message: db.Column(db.String(2000))
    sent_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    
    # Foregin Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    

```

Channel

```py
from datetime import datetime
from ..dev import db


class Channel(db.Model):
    __tablename__ = "channels"
    # Table Keys
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000))
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    
    # Foreign Keys
    team_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
```

Teams

```py
from datetime import datetime
from ..dev import db


class Team(db.Model):
    __tablename__ = "teams"
    # Table Keys
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
```

Join Tables (Memberships)

Channel

```py
from datetime import datetime
from ...dev import db


class channel_membership:
    __tablename__ = "channel_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type: db.Column(db.String(150))
    joined_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
```

Team

```py
from datetime import datetime
from ...dev import db


class team_membership:
    __tablename__ = "team_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type: db.Column(db.String(150))
    joined_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
```
