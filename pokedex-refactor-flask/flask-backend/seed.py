import json
import random
from app import app
from app.models import Item, Pokemon, db

with app.app_context():
    db.drop.all()
    db.create.all()

    f = open('pokemon.json')
    data = json.load(f)

    for p in data:
        pokemon = Pokemon(
            number=p['number'],
            imageUrl=p['imageUrl'],
            name=p['name'],
            attack=p['attack'],
            defense=p['defense'],
            type=p['type'],
            moves=','.join(p['moves']),
            captured=p['captured'] if len(p) == 8 else False
        )

        # pokemon = Pokemon(p)
        # print(pokemon)
        db.session.add(pokemon)

    f.close()

    def random_image():
        images = [
            "/images/pokemon_berry.svg",
            "/images/pokemon_egg.svg",
            "/images/pokemon_potion.svg",
            "/images/pokemon_super_potion.svg",
        ]

        return random.choice(images)

    def random_item():
        items = [
            'berry',
            'egg',
            'potion',
            'super potion',
        ]

        return random.choice(items)

    for pokemonId in range(125):
        for _ in range(3):
            item = Item(
                happiness=random.randint(1, 100),
                price=random.randint(1, 100),
                imageUrl=random_image(),
                name=random_item(),
                pokemonId=pokemonId,
            )

            db.session.add(item)

    db.session.commit()
