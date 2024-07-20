from django.test import TestCase

from ..models import Game
from .factories import GameFactory

class GameTestCase(TestCase):
    def test_str(self):
        """Test that the representation of Game is str"""
        game = GameFactory()
        self.assertEqual(str(game), game.title)
