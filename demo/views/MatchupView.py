import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from demo.delegates.MatchupDelegate import MatchupDelegate

 #======================================================================
# 
# Encapsulates data for View Matchup
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class MatchupView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Matchup index.")

def get(request, matchupId ):
	delegate = MatchupDelegate()
	responseData = delegate.get( matchupId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	matchup = json.loads(request.body)
	delegate = MatchupDelegate()
	responseData = delegate.createFromJson( matchup )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	matchup = json.loads(request.body)
	delegate = MatchupDelegate()
	responseData = delegate.save( matchup )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, matchupId ):
	delegate = MatchupDelegate()
	responseData = delegate.delete( matchupId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = MatchupDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def addGames( request, matchupId, GamesIds ):
	delegate = MatchupDelegate()
	responseData = delegate.addGames( matchupId, GamesIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def removeGames( request, matchupId, GamesIds ):
	delegate = MatchupDelegate()
	responseData = delegate.removeGames( matchupId, GamesIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

