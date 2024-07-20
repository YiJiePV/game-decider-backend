from django.test import TestCase

from ..serializers import GameSerializer
from .factories import GameFactory

class GameSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches a Game for each field."""
        game = GameFactory()
        for field_name in [
            'id', 'title', 'summary'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(game, field_name)
            )
