from django.urls import path
from demo.views import MatchupView

urlpatterns = [
    path('', MatchupView.index, name='index'),
	path('create', MatchupView.get, name='create'),
	path('get/<int:matchupId>/', MatchupView.get, name='get'),
	path('save', MatchupView.save, name='save'),
	path('getAll', MatchupView.getAll, name='getAll'),
	path('delete/<int:matchupId>/', MatchupView.delete, name='delete'),
	path('addGames/<int:matchupId>/<GamesIds>/', MatchupView.addGames, name='addGames'),
	path('removeGames/<int:matchupId>/<GamesIds>/', MatchupView.removeGames, name='removeGames'),
]
