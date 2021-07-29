from django.urls import path
from demo.views import LeagueView

urlpatterns = [
    path('', LeagueView.index, name='index'),
	path('create', LeagueView.get, name='create'),
	path('get/<int:leagueId>/', LeagueView.get, name='get'),
	path('save', LeagueView.save, name='save'),
	path('getAll', LeagueView.getAll, name='getAll'),
	path('delete/<int:leagueId>/', LeagueView.delete, name='delete'),
	path('addPlayers/<int:leagueId>/<PlayersIds>/', LeagueView.addPlayers, name='addPlayers'),
	path('removePlayers/<int:leagueId>/<PlayersIds>/', LeagueView.removePlayers, name='removePlayers'),
]
