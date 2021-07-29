from django.urls import path
from demo.views import TournamentView

urlpatterns = [
    path('', TournamentView.index, name='index'),
	path('create', TournamentView.get, name='create'),
	path('get/<int:tournamentId>/', TournamentView.get, name='get'),
	path('save', TournamentView.save, name='save'),
	path('getAll', TournamentView.getAll, name='getAll'),
	path('delete/<int:tournamentId>/', TournamentView.delete, name='delete'),
	path('addMatchups/<int:tournamentId>/<MatchupsIds>/', TournamentView.addMatchups, name='addMatchups'),
	path('removeMatchups/<int:tournamentId>/<MatchupsIds>/', TournamentView.removeMatchups, name='removeMatchups'),
]
