from django.contrib import admin
from .models import Game

# setting up game info to display in the Django admin interface (testing purposes)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

# Register your models here.

admin.site.register(Game, GameAdmin)
