from django.db import models

#======================================================================
# 
# Encapsulates data for model Game
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class Game Declaration
#======================================================================
class Game (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	frames = models.IntegerField(null=True)
	matchup = models.ForeignKey('Matchup', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	player = models.OneToOneField('Player', on_delete=models.CASCADE, null=True, blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.frames
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Game";
    
	def objectType(self):
		return "Game";
