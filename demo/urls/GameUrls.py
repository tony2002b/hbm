from django.urls import path
from demo.views import GameView

urlpatterns = [
    path('', GameView.index, name='index'),
	path('create', GameView.get, name='create'),
	path('get/<int:gameId>/', GameView.get, name='get'),
	path('save', GameView.save, name='save'),
	path('getAll', GameView.getAll, name='getAll'),
	path('delete/<int:gameId>/', GameView.delete, name='delete'),
	path('assignMatchup/<int:gameId>/<int:MatchupId>/', GameView.assignMatchup, name='assignMatchup'),
	path('unassignMatchup/<int:gameId>/', GameView.unassignMatchup, name='unassignMatchup'),
	path('assignPlayer/<int:gameId>/<int:PlayerId>/', GameView.assignPlayer, name='assignPlayer'),
	path('unassignPlayer/<int:gameId>/', GameView.unassignPlayer, name='unassignPlayer'),
]
