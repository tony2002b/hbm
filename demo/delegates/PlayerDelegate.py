from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from demo.models.Player import Player
from demo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Player
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class PlayerDelegate Declaration
#======================================================================
class PlayerDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, playerId ):
		try:	
			player = Player.objects.filter(id=playerId)
			return player.first();
		except Player.DoesNotExist:
			raise ProcessingError("Player with id " + str(playerId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, player):
		for model in serializers.deserialize("json", player):
			model.save()
			return model;

	def create(self, player):
		player.save()
		return player;

	def saveFromJson(self, player):
		for model in serializers.deserialize("json", player):
			model.save()
			return player;
	
	def save(self, player):
		player.save()
		return player;
	
	def delete(self, playerId ):
		errMsg = "Failed to delete Player from db using id " + str(playerId)
		
		try:
			player = Player.objects.get(id=playerId)
			player.delete()
			return True
		except Player.DoesNotExist:
			raise ProcessingError("Player with id " + str(playerId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Player.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Player from db")
		except Exception:
			return None;
		
