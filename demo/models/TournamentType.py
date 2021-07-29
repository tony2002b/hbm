from django.db import models
 #======================================================================
# 
# Encapsulates data for model TournamentType
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class TournamentType Declaration (enumerated type)
#======================================================================
from enum import Enum 
class TournamentType(Enum):   # A subclass of Enum
	Pro = 'Pro'
	Amateur = 'Amateur'
