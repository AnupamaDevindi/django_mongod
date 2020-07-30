import pymongo
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view

import TrackSystem

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.ee3da.mongodb.net/anklet?retryWrites=true&w=majority")

database = client["track_system"]
Collection = database["track_system.total_sprints(cleaned)"]


@api_view(['GET', 'POST', 'DELETE'])
def track_list(request):

    return HttpResponse("Hi..Success")

    # GET / PUT / DELETE tutorial
