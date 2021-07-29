from django.db import models

#======================================================================
# 
# Encapsulates data for model League
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class League Declaration
#======================================================================
class League (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	name = models.CharField(max_length=200, null=True)
	players = models.ManyToManyField('Player',  blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "League";
    
	def objectType(self):
		return "League";
