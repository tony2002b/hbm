from django.db import models
from demo.models.TournamentType import TournamentType

#======================================================================
# 
# Encapsulates data for model Tournament
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class Tournament Declaration
#======================================================================
class Tournament (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	name = models.CharField(max_length=200, null=True)
	matchups = models.ManyToManyField('Matchup',  blank=True, related_name='+')
	type = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in TournamentType])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		str = str + self.type
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Tournament";
    
	def objectType(self):
		return "Tournament";
