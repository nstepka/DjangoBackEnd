from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api import models
from api.models import ( AbcResource,  Inventory, ResourceType, InventoryDDL)
from api.serializers import ( Abc_resourceSerializer, Inventory_typeSerializer, Resource_typeSerializer, InventoryDDL_typeSerializer)

@csrf_exempt
def abcResourceApi(request):
    if request.method == 'GET':
       abcResources = models.AbcResource.objects.all()
       aabcResources_serializer = Abc_resourceSerializer(abcResources, many=True)
       return JsonResponse(aabcResources_serializer.data, safe=False)
    elif request.method == 'POST':
        abcResource_data = JSONParser().parse(request)
        abcResources_serializer = Abc_resourceSerializer(data=abcResource_data)
        if abcResources_serializer.is_valid():
            abcResources_serializer.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to Add abcresource", safe=False)
    elif request.method == 'PUT':
        abcResources_data = JSONParser().parse(request)
        abcResources = AbcResource.objects.get(
            abc_resource_id=abcResources_data['abc_resource_id'])
        abcResources_serializer = Abc_resourceSerializer(
            abcResources, data=abcResources_data)
        if abcResources_serializer.is_valid():
            abcResources_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        abcResource = AbcResource.objects.get(abc_resource_id=id)
        abcResource.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def resourceTypeApi(request):
    if request.method=='GET':
        resourceTypes = models.ResourceType.objects.all()
        resourceType_serializer = Resource_typeSerializer(resourceTypes,many=True)
        return JsonResponse(resourceType_serializer.data,safe=False)
    elif request.method=='POST':
        resourceTypes_data=JSONParser().parse(request)
        resourceTypes_serializer = Resource_typeSerializer(data=resourceTypes_data)
        if resourceTypes_serializer.is_valid():
            resourceTypes_serializer.save()
            return JsonResponse("Added Successfull",safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        resourceTypes_data = JSONParser().parse(request)
        resourceType = ResourceType.objects.get(resource_type_id=resourceTypes_data['resource_type_id'])
        resourceType_serializer = Resource_typeSerializer(resourceType,data=resourceTypes_data)
        if resourceType_serializer.is_valid():
            resourceType_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")    

@csrf_exempt
def inventoryApi(request):
    if request.method=='GET':
        inventories = Inventory.objects.all()
        inventory_serializer = Inventory_typeSerializer(inventories,many=True)
        return JsonResponse(inventory_serializer.data,safe=False)
    elif request.method=='POST':
        inventory_data=JSONParser().parse(request)
        inventory_serializer = Inventory_typeSerializer(data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse("Added Inventory Successfull",safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        inventory_data = JSONParser().parse(request)
        inventory = ResourceType.objects.get(inventory_id=inventory_data['inventory_id'])
        inventory_serializer = Inventory_typeSerializer(inventory,data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")

@csrf_exempt
def inventoryDDLApi(request):
    if request.method=='GET':
        inventoriesDDL = InventoryDDL.objects.all()
        inventoryDDL_serializer = InventoryDDL_typeSerializer(inventoriesDDL,many=True)
        return JsonResponse(inventoryDDL_serializer.data,safe=False)
    elif request.method=='POST':
        inventoryDDL_data=JSONParser().parse(request)
        inventoryDDL_serializer = InventoryDDL_typeSerializer(data=inventoryDDL_data)
        if inventoryDDL_serializer.is_valid():
            inventoryDDL_serializer.save()
            return JsonResponse("Added Inventory Successfull",safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        inventoryDDL_data = JSONParser().parse(request)
        inventoryDDL = ResourceType.objects.get(inventory_id=inventoryDDL['inventory_id'])
        inventoryDDL_serializer = InventoryDDL_typeSerializer(inventoryDDL,data=inventoryDDL_data)
        if inventoryDDL_serializer.is_valid():
            inventoryDDL_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")


## create new function for retrieving all inventory ids /api/inventory_id
