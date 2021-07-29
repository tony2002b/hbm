from django.urls import path
from demo.views import PlayerView

urlpatterns = [
    path('', PlayerView.index, name='index'),
	path('create', PlayerView.get, name='create'),
	path('get/<int:playerId>/', PlayerView.get, name='get'),
	path('save', PlayerView.save, name='save'),
	path('getAll', PlayerView.getAll, name='getAll'),
	path('delete/<int:playerId>/', PlayerView.delete, name='delete'),
]
