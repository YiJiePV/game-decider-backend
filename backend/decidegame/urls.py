from django.urls import path, include
from .views import (
    ViewAllIds,
    ViewAllGames,
    ViewOneGame,
    AddAGame,
    UpdateAGame,
    DeleteAGame,
)

urlpatterns = [
    path('api/<int:game_id>/', ViewOneGame.as_view()),
    path('api/ids/', ViewAllIds.as_view()),
    path('api', ViewAllGames.as_view()),
    path('api/add/', AddAGame.as_view()),
    path('api/update/<int:game_id>/', UpdateAGame.as_view()),
    path('api/delete/<int:game_id>/', DeleteAGame.as_view()),
]
