import datetime

from django.test import TestCase
from django.utils import timezone
from demo.models.Tournament import Tournament
from demo.delegates.TournamentDelegate import TournamentDelegate

 #======================================================================
# 
# Encapsulates data for model Tournament
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class TournamentTest Declaration
#======================================================================
class TournamentTest (TestCase) :
	def test_crud(self) :
		tournament = Tournament()
		tournament.name = "default name field value"
		tournament.type = "default type field value"
		
		delegate = TournamentDelegate()
		responseObj = delegate.create(tournament)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


