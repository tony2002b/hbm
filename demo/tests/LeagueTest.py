import datetime

from django.test import TestCase
from django.utils import timezone
from demo.models.League import League
from demo.delegates.LeagueDelegate import LeagueDelegate

 #======================================================================
# 
# Encapsulates data for model League
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class LeagueTest Declaration
#======================================================================
class LeagueTest (TestCase) :
	def test_crud(self) :
		league = League()
		league.name = "default name field value"
		
		delegate = LeagueDelegate()
		responseObj = delegate.create(league)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


