import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from demo.delegates.LeagueDelegate import LeagueDelegate

 #======================================================================
# 
# Encapsulates data for View League
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class LeagueView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the League index.")

def get(request, leagueId ):
	delegate = LeagueDelegate()
	responseData = delegate.get( leagueId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	league = json.loads(request.body)
	delegate = LeagueDelegate()
	responseData = delegate.createFromJson( league )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	league = json.loads(request.body)
	delegate = LeagueDelegate()
	responseData = delegate.save( league )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, leagueId ):
	delegate = LeagueDelegate()
	responseData = delegate.delete( leagueId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = LeagueDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def addPlayers( request, leagueId, PlayersIds ):
	delegate = LeagueDelegate()
	responseData = delegate.addPlayers( leagueId, PlayersIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def removePlayers( request, leagueId, PlayersIds ):
	delegate = LeagueDelegate()
	responseData = delegate.removePlayers( leagueId, PlayersIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

