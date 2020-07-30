from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json
import pymongo
from django.http import JsonResponse
from bson.json_util import loads
from django.views.decorators.csrf import csrf_exempt
from bson import BSON

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.ee3da.mongodb.net/anklet?retryWrites=true&w=majority")
# db = client.test
mydb = client["anklet"]
mycol = mydb["anklet.ankletLeft_raw"]

@csrf_exempt
def index(request):

    # listOfDB = client.list_database_names()
    # return JsonResponse(listOfDB, safe=False)
    #x = '{ "name":"John", "age":30, "city":"New York"}'

    # dataJson = {  "device":"ankletLeft",             
    #               "sensorData" : [{
    #                         "recNo": 0,
    #                         "time": 10.02,
    #                         "Ax": 0,
    #                         "Ay": 0,
    #                         "Az": 0,
    #                         "T": 39.54176,
    #                         "Gx": 0,
    #                         "Gy": 0,
    #                         "Gz": 0
    #                     },
    #                     {
    #                         "recNo": 1,
    #                         "time": 10.02,
    #                         "Ax": 0.088135,
    #                         "Ay": -0.077637,
    #                         "Az": 0.97876,
    #                         "T": 31.16529,
    #                         "Gx": 1.992366,
    #                         "Gy": 1.122137,
    #                         "Gz": -1.320611
    #                     },
    #                     {
    #                         "recNo": 2,
    #                         "time": 10.02,
    #                         "Ax": 0.081787,
    #                         "Ay": -0.06543,
    #                         "Az": 0.951416,
    #                         "T": 31.35353,
    #                         "Gx": -0.030534,
    #                         "Gy": 2.167939,
    #                         "Gz": -2.129771
    #                     },
    #                     {
    #                         "recNo": 3,
    #                         "time": 10.02,
    #                         "Ax": 0.091309,
    #                         "Ay": -0.070801,
    #                         "Az": 0.943604,
    #                         "T": 31.25941,
    #                         "Gx": -0.267176,
    #                         "Gy": 2.854962,
    #                         "Gz": -1.847328
    #                     },
    #                     {
    #                         "recNo": 4,
    #                         "time": 10.02,
    #                         "Ax": 0.09668,
    #                         "Ay": -0.059326,
    #                         "Az": 0.931397,
    #                         "T": 31.35353,
    #                         "Gx": -0.183206,
    #                         "Gy": 6.351145,
    #                         "Gz": -1.656489
    #                     }
    #                 ]
    # }


    #
    #jsonData = request.body
    jsonData = json.loads(request.body)
    mycol.insert_one(jsonData)
    
    return HttpResponse("Inserted to DB successfully")

    #jsonData = json.dumps(jsonData)
    #bson_example = BSON.encode({"Object":jsonData})

    # jsonData = { "name": "John", "address":jsonData }

    # datajas = {"data":request.data}

    

    #mycol.insert_one(request.read())
    #mycol.insert_one(dataJson)

    # insertID = x.inserted_id
    # return JsonResponse(insertID, safe=False)
    #return HttpResponse("Hello, world. You're at the anklet index.")

    #return JsonResponse(request, safe=False)


    #return JsonResponse(jsonData, safe=False)

    #mycol.insert_one(request.read())
    #return HttpResponse(request.read())



    #return HttpResponse(request.body)

    #return HttpResponse(jsonData)
    # return HttpResponse(bson_example)
    #return HttpResponse(dataJson)
    #return HttpResponse(request)

def raw(request):
    return HttpResponse("Hello, world. You're at the anklet raw.")