from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from demo.models.League import League
from demo.models.Player import Player
from demo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model League
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class LeagueDelegate Declaration
#======================================================================
class LeagueDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, leagueId ):
		try:	
			league = League.objects.filter(id=leagueId)
			return league.first();
		except League.DoesNotExist:
			raise ProcessingError("League with id " + str(leagueId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, league):
		for model in serializers.deserialize("json", league):
			model.save()
			return model;

	def create(self, league):
		league.save()
		return league;

	def saveFromJson(self, league):
		for model in serializers.deserialize("json", league):
			model.save()
			return league;
	
	def save(self, league):
		league.save()
		return league;
	
	def delete(self, leagueId ):
		errMsg = "Failed to delete League from db using id " + str(leagueId)
		
		try:
			league = League.objects.get(id=leagueId)
			league.delete()
			return True
		except League.DoesNotExist:
			raise ProcessingError("League with id " + str(leagueId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = League.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all League from db")
		except Exception:
			return None;
		
	def addPlayers( self, leagueId, playersIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.PlayerDelegate import PlayerDelegate

		errMsg = "Failed to add elements " + str(playersIds) + " for Players on League"

		try:
			# get the League
			league = self.get( leagueId ).first()
				
			# split on a comma with no spaces
			idList = playersIds.split(',')

			
			# iterate over ids
			for id in idList:
				# read the Player		
				player = PlayerDelegate().get(id).first();	
				# add the Player
				league.players.add(player)
				
			# save it		
			league.save()
			
			# reload and return the appropriate version
			return self.get( leagueId );
		except League.DoesNotExist:
			raise ProcessingError(errMsg + " : League with id " + str(leagueId) + " does not exist.")
		except Player.DoesNotExist:
			raise ProcessingError(errMsg + " : Player does not exist.")
		except Exception:
			raise ProcessingError(errMsg) 
		
	def removePlayers( self, leagueId, playersIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.PlayerDelegate import PlayerDelegate

		errMsg = "Failed to remove elements " + str(playersIds) + " for Players on League"

		try:
			# get the League
			league = self.get( leagueId ).first()
				
			# split on a comma with no spaces
			idList = playersIds.split(',')
			
			# iterate over ids
			for id in idList:
				# read the Player		
				player = PlayerDelegate().get(id).first();	
				# add the Player
				league.players.remove(player)
				
			# save it		
			league.save()
			
			# reload and return the appropriate version
			return self.get( leagueId );
		except League.DoesNotExist:
			raise ProcessingError(errMsg + " : League with id " + str(leagueId) + " does not exist.")
		except Player.DoesNotExist:
			raise ProcessingError(errMsg + " : Player does not exist.")
		except utils.DatabaseError:
			raise StorageWriteError()
		except Exception:
			raise GeneralError(errMsg) 
		
