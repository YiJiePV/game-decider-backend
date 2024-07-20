from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GameSerializer, IdSerializer
from .models import Game

# Create your views here.

class ViewAllGames(APIView):
    # Get all games
    def get(self, *args, **kwargs):
        '''
        Gets all games
        '''
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewAllIds(APIView):
    # Get only ID of all games
    def get(self, *args, **kwargs):
        '''
        Gets only game IDs
        '''
        games = Game.objects.all()
        serializer = IdSerializer(games, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewOneGame(APIView):
    # get one game given ID
    def get(self, request, game_id, *args, **kwargs):
            try:
                game_instance = Game.objects.get(id=game_id)
                serializer = GameSerializer(game_instance)
                return Response(serializer.data, status=status.HTTP_200_OK) 
            except Game.DoesNotExist:
                return Response(
                    {"res": f"Game with ID {game_id} does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
class AddAGame(APIView):
    # Add a game (implement later)
    def post(self, request, *args, **kwargs):
        '''
        Add a new game
        '''
        data = {
            'title': request.data.get('title'),
            'summary': request.data.get('summary')
        }

        serializer = GameSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateAGame(APIView):
    def put(self, request, game_id, *args, **kwargs):
        '''
        Update a game with the given ID
        '''
        try:
            game_instance = Game.objects.get(id=game_id)

            data = {
                'title': request.data.get('title'),
                'summary': request.data.get('summary')
            }

            serializer = GameSerializer(instance = game_instance, data=data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Game.DoesNotExist:
            return Response(
                {"res": f"Game with ID {game_id} does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class DeleteAGame(APIView):
    def delete(self, request, game_id, *args, **kwargs):
        '''
        Delete a game with the given ID
        '''
        try:
            game_instance = Game.objects.get(id=game_id)

            game_instance.delete()

            return Response(
                {"res": "Game deleted!"},
                status=status.HTTP_200_OK
            )
        
        except Game.DoesNotExist:
            return Response(
                {"res": f"Game with ID {game_id} does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        