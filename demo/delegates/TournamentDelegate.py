from django.core import exceptions
from django.core import serializers
from django.db import models
from django.db import utils

from demo.models.Tournament import Tournament
from demo.models.Matchup import Matchup
from demo.exceptions import Exceptions

 #======================================================================
# 
# Encapsulates data for model Tournament
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class TournamentDelegate Declaration
#======================================================================
class TournamentDelegate :

#======================================================================
# Function Declarations
#======================================================================

	def get(self, tournamentId ):
		try:	
			tournament = Tournament.objects.filter(id=tournamentId)
			return tournament.first();
		except Tournament.DoesNotExist:
			raise ProcessingError("Tournament with id " + str(tournamentId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 

	def createFromJson(self, tournament):
		for model in serializers.deserialize("json", tournament):
			model.save()
			return model;

	def create(self, tournament):
		tournament.save()
		return tournament;

	def saveFromJson(self, tournament):
		for model in serializers.deserialize("json", tournament):
			model.save()
			return tournament;
	
	def save(self, tournament):
		tournament.save()
		return tournament;
	
	def delete(self, tournamentId ):
		errMsg = "Failed to delete Tournament from db using id " + str(tournamentId)
		
		try:
			tournament = Tournament.objects.get(id=tournamentId)
			tournament.delete()
			return True
		except Tournament.DoesNotExist:
			raise ProcessingError("Tournament with id " + str(tournamentId) + " does not exist.")
		except utils.DatabaseError:
			raise StorageReadError()
		except Exception:
			raise GeneralError(errMsg) 
	
	def getAll(self):
		try:
			all = Tournament.objects.all()
			return all;
		except utils.DatabaseError:
			raise StorageReadError("Failed to get all Tournament from db")
		except Exception:
			return None;
		
	def addMatchups( self, tournamentId, matchupsIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.MatchupDelegate import MatchupDelegate

		errMsg = "Failed to add elements " + str(matchupsIds) + " for Matchups on Tournament"

		try:
			# get the Tournament
			tournament = self.get( tournamentId ).first()
				
			# split on a comma with no spaces
			idList = matchupsIds.split(',')

			
			# iterate over ids
			for id in idList:
				# read the Matchup		
				matchup = MatchupDelegate().get(id).first();	
				# add the Matchup
				tournament.matchups.add(matchup)
				
			# save it		
			tournament.save()
			
			# reload and return the appropriate version
			return self.get( tournamentId );
		except Tournament.DoesNotExist:
			raise ProcessingError(errMsg + " : Tournament with id " + str(tournamentId) + " does not exist.")
		except Matchup.DoesNotExist:
			raise ProcessingError(errMsg + " : Matchup does not exist.")
		except Exception:
			raise ProcessingError(errMsg) 
		
	def removeMatchups( self, tournamentId, matchupsIds ):
		# lazy importing avoids circular dependencies
		from demo.delegates.MatchupDelegate import MatchupDelegate

		errMsg = "Failed to remove elements " + str(matchupsIds) + " for Matchups on Tournament"

		try:
			# get the Tournament
			tournament = self.get( tournamentId ).first()
				
			# split on a comma with no spaces
			idList = matchupsIds.split(',')
			
			# iterate over ids
			for id in idList:
				# read the Matchup		
				matchup = MatchupDelegate().get(id).first();	
				# add the Matchup
				tournament.matchups.remove(matchup)
				
			# save it		
			tournament.save()
			
			# reload and return the appropriate version
			return self.get( tournamentId );
		except Tournament.DoesNotExist:
			raise ProcessingError(errMsg + " : Tournament with id " + str(tournamentId) + " does not exist.")
		except Matchup.DoesNotExist:
			raise ProcessingError(errMsg + " : Matchup does not exist.")
		except utils.DatabaseError:
			raise StorageWriteError()
		except Exception:
			raise GeneralError(errMsg) 
		
