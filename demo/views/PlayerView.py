import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from demo.delegates.PlayerDelegate import PlayerDelegate

 #======================================================================
# 
# Encapsulates data for View Player
#
# @author your_name_here
#
#======================================================================

#======================================================================
# Class PlayerView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Player index.")

def get(request, playerId ):
	delegate = PlayerDelegate()
	responseData = delegate.get( playerId )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def create(request):
	player = json.loads(request.body)
	delegate = PlayerDelegate()
	responseData = delegate.createFromJson( player )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	player = json.loads(request.body)
	delegate = PlayerDelegate()
	responseData = delegate.save( player )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def delete(request, playerId ):
	delegate = PlayerDelegate()
	responseData = delegate.delete( playerId )
	return HttpResponse(responseData, content_type="application/json");

def getAll(request):
	delegate = PlayerDelegate()
	responseData = delegate.getAll()
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

