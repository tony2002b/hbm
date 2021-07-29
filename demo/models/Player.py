from django.db import models

#======================================================================
# 
# Encapsulates data for model Player
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class Player Declaration
#======================================================================
class Player (models.Model):

#======================================================================
# attribute declarations
#======================================================================
	name = models.CharField(max_length=200, null=True)
	dateOfBirth = models.DateField(null=True)
	height = models.DecimalField(max_digits=12, decimal_places=4, null=True)
	isProfessional = models.BooleanField(null=True)

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		str = str + self.dateOfBirth
		str = str + self.height
		str = str + self.isProfessional
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Player";
    
	def objectType(self):
		return "Player";
