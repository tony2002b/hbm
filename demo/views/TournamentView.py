import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from demo.delegates.TournamentDelegate import TournamentDelegate

 #======================================================================
# 
# Encapsulates data for View Tournament
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class TournamentView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Tournament index.")

def get(request, tournamentId ):
	delegate = TournamentDelegate()
	responseData = delegate.get( tournamentId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	tournament = json.loads(request.body)
	delegate = TournamentDelegate()
	responseData = delegate.createFromJson( tournament )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	tournament = json.loads(request.body)
	delegate = TournamentDelegate()
	responseData = delegate.save( tournament )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, tournamentId ):
	delegate = TournamentDelegate()
	responseData = delegate.delete( tournamentId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = TournamentDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def addMatchups( request, tournamentId, MatchupsIds ):
	delegate = TournamentDelegate()
	responseData = delegate.addMatchups( tournamentId, MatchupsIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def removeMatchups( request, tournamentId, MatchupsIds ):
	delegate = TournamentDelegate()
	responseData = delegate.removeMatchups( tournamentId, MatchupsIds )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

