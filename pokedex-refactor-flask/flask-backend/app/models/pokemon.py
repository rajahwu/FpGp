from . import db


class Pokemon(db.Model):
    __tablename__ = "pokemen"

    TYPES = [
        "fire",
        "electric",
        "normal",
        "ghost",
        "psychic",
        "water",
        "bug",
        "dragon",
        "grass",
        "fighting",
        "ice",
        "flying",
        "poison",
        "ground",
        "rock",
        "steel",
    ]

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.Enum(*TYPES), name='type', nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Numeric(3, 2), nullable=False, default=1.00)
    catchRate = db.Column(db.Numeric(3, 2), nullable=False, default=1.00)
    captured = db.Column(db.Boolean)
