from factory import DjangoModelFactory, Faker

from ..models import Game

class GameFactory(DjangoModelFactory):
    title = Faker('game')
    summary = Faker('text')

    class Meta:
        model = Game
