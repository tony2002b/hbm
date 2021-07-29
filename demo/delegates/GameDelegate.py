from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from demo.models.Game import Game
from demo.models.Matchup import Matchup
from demo.models.Player import Player
from demo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Game
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class GameDelegate Declaration
#======================================================================
class GameDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, gameId ):
		try:	
			game = Game.objects.filter(id=gameId)
			return game.first();
		except Game.DoesNotExist:
			raise ProcessingError("Game with id " + str(gameId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, game):
		for model in serializers.deserialize("json", game):
			model.save()
			return model;

	def create(self, game):
		game.save()
		return game;

	def saveFromJson(self, game):
		for model in serializers.deserialize("json", game):
			model.save()
			return game;
	
	def save(self, game):
		game.save()
		return game;
	
	def delete(self, gameId ):
		errMsg = "Failed to delete Game from db using id " + str(gameId)
		
		try:
			game = Game.objects.get(id=gameId)
			game.delete()
			return True
		except Game.DoesNotExist:
			raise ProcessingError("Game with id " + str(gameId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Game.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Game from db")
		except Exception:
			return None;
		
	def assignMatchup( self, gameId, matchupId ):
		# lazy importing avoids circular dependencies
		from demo.delegates.MatchupDelegate import MatchupDelegate

		errMsg = "Failed to assign element " + str(matchupId) + " for Matchup on Game"

		try:
			# get the Game from db
			game = self.get( gameId ).first()	
			
			# get the Matchup from db
			matchup = MatchupDelegate().get(matchupId).first();
			
			# assign the Matchup		
			game.matchup = matchup
			
			#save it
			game.save()

			# reload and return the appropriate version					
			return self.get( gameId );
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game with id " + str(gameId) + " does not exist.")
		except Matchup.DoesNotExist:
			raise ProcessingError(errMsg + " : Matchup with id " + str(matchupId) + " does not exist.")
		except Exception:
			return None;
				
	def unassignMatchup( self, gameId ):
		errMsg = "Failed to unassign element " + str(matchupId) + " for Matchup on Game"

		try:
			# get the Game from db
			game = self.get( gameId ).first()	
			
			# assign to None for unassignment
			game.matchup = None			

			#save it
			game.save()

			# reload and return the appropriate version					
			return self.get( gameId );
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game with id " + str(gameId) + " does not exist.")
		except Exception:
			return None;
		
	def assignPlayer( self, gameId, playerId ):
		# lazy importing avoids circular dependencies
		from demo.delegates.PlayerDelegate import PlayerDelegate

		errMsg = "Failed to assign element " + str(playerId) + " for Player on Game"

		try:
			# get the Game from db
			game = self.get( gameId ).first()	
			
			# get the Player from db
			player = PlayerDelegate().get(playerId).first();
			
			# assign the Player		
			game.player = player
			
			#save it
			game.save()

			# reload and return the appropriate version					
			return self.get( gameId );
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game with id " + str(gameId) + " does not exist.")
		except Player.DoesNotExist:
			raise ProcessingError(errMsg + " : Player with id " + str(playerId) + " does not exist.")
		except Exception:
			return None;
				
	def unassignPlayer( self, gameId ):
		errMsg = "Failed to unassign element " + str(playerId) + " for Player on Game"

		try:
			# get the Game from db
			game = self.get( gameId ).first()	
			
			# assign to None for unassignment
			game.player = None			

			#save it
			game.save()

			# reload and return the appropriate version					
			return self.get( gameId );
		except Game.DoesNotExist:
			raise ProcessingError(errMsg + " : Game with id " + str(gameId) + " does not exist.")
		except Exception:
			return None;
		
