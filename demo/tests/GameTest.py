import datetime

from django.test import TestCase
from django.utils import timezone
from demo.models.Game import Game
from demo.delegates.GameDelegate import GameDelegate

 #======================================================================
# 
# Encapsulates data for model Game
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class GameTest Declaration
#======================================================================
class GameTest (TestCase) :
	def test_crud(self) :
		game = Game()
		game.frames = 22
		
		delegate = GameDelegate()
		responseObj = delegate.create(game)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


