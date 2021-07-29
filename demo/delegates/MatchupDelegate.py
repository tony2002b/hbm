from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from demo.models.Matchup import Matchup
from demo.models.Game import Game
from demo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Matchup
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class MatchupDelegate Declaration
#======================================================================
class MatchupDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, matchupId ):
		try:	
			matchup = Matchup.objects.filter(id=matchupId)
			return matchup.first();
		except Matchup.DoesNotExist:
			raise ProcessingError("Matchup with id " + str(matchupId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, matchup):
		for model in serializers.deserialize("json", matchup):
			model.save()
			return model;

	def create(self, matchup):
		matchup.save()
		return matchup;

	def saveFromJson(self, matchup):
		for model in serializers.deserialize("json", matchup):
			model.save()
			return matchup;
	
	def save(self, matchup):
		matchup.save()
		return matchup;
	
	def delete(self, matchupId ):
		errMsg = "Failed to delete Matchup from db using id " + str(matchupId)
		
		try:
			matchup = Matchup.objects.get(id=matchupId)
			matchup.delete()
			return True
		except Matchup.DoesNotExist:
			raise ProcessingError("Matchup with id " + str(matchupId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Matchup.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Matchup from db")
		except Exception:
			return None;
		
	def addGames( self, matchupId, gamesIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.GameDelegate import GameDelegate

		errMsg = "Failed to add elements " + str(gamesIds) + " for Games on Matchup"

		try:
			# get the Matchup
			matchup = self.get( matchupId ).first()
				
			# split on a comma with no spaces
			idList = gamesIds.split(',')

			
			# iterate over ids
			for id in idList:
				# read the Game		
				game = GameDelegate().get(id).first();	
				# add the Game
				matchup.games.add(game)
				
			# save it		
			matchup.save()
			
			# reload and return the appropriate version
			return self.get( matchupId );
		except Matchup.DoesNotExist:
			raise ProcessingError(errMsg + " : Matchup with id " + str(matchupId) + " does not exist.")
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game does not exist.")
		except Exception:
			raise ProcessingError(errMsg) 
		
	def removeGames( self, matchupId, gamesIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.GameDelegate import GameDelegate

		errMsg = "Failed to remove elements " + str(gamesIds) + " for Games on Matchup"

		try:
			# get the Matchup
			matchup = self.get( matchupId ).first()
				
			# split on a comma with no spaces
			idList = gamesIds.split(',')
			
			# iterate over ids
			for id in idList:
				# read the Game		
				game = GameDelegate().get(id).first();	
				# add the Game
				matchup.games.remove(game)
				
			# save it		
			matchup.save()
			
			# reload and return the appropriate version
			return self.get( matchupId );
		except Matchup.DoesNotExist:
			raise ProcessingError(errMsg + " : Matchup with id " + str(matchupId) + " does not exist.")
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game does not exist.")
		except utils.DatabaseError:
			raise StorageWriteError()
		except Exception:
			raise GeneralError(errMsg) 
		
