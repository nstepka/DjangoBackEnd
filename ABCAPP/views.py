from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ABCAPP import models
from ABCAPP.models import (AbcClient, AbcResource, AccessLog, Address,
                           ClientContacts, Contact, Inventory, ResourceType,
                           StorageType)
from ABCAPP.serializers import (Abc_clientSerializer, Abc_resourceSerializer,
                                AddressSerializer, ContactSerializer,
                                Inventory_typeSerializer,
                                Resource_typeSerializer,
                                Storage_typeSerializer, access_logSerializer)

# Create your views here.


@csrf_exempt
def abcclientApi(request):
    if request.method == 'GET':
        abcClients = models.AbcClient.objects.all()
        abcClient_serializer = Abc_clientSerializer(abcClients, many=True)
        return JsonResponse(abcClient_serializer.data, safe=False)
    elif request.method == 'POST':
        abcClient_data = JSONParser().parse(request)
        abcClient_serializer = Abc_clientSerializer(data=abcClient_data)
        if abcClient_serializer.is_valid():
            abcClient_serializer.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        abcClient_data = JSONParser().parse(request)
        abcClient = AbcClient.objects.get(
            abc_client_id=abcClient_data['abc_client_id'])
        abcClient_serializer = Abc_clientSerializer(
            abcClient, data=abcClient_data)
        if abcClient_serializer.is_valid():
            abcClient_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        abcClient = AbcClient.objects.get(abc_client_id=id)
        abcClient.delete()
        return JsonResponse("Deleted Successfully", safe=False)

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
def addressApi(request):
    if request.method=='GET':
        addresses = models.Address.objects.all()
        addresses_serializer = AddressSerializer(addresses,many=True)
        return JsonResponse(addresses_serializer.data,safe=False)
    elif request.method=='POST':
        address_data=JSONParser().parse(request)
        addresses_serializer = AddressSerializer(data=address_data)
        if addresses_serializer.is_valid():
            addresses_serializer.save()
            return JsonResponse("Added Successfull",safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        address_data = JSONParser().parse(request)
        address = Address.objects.get(address_id=address_data['address_id'])
        addresses_serializer = AddressSerializer(address,data=address_data)
        if addresses_serializer.is_valid():
            addresses_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("failed to update")    
    elif request.method=='DELETE':
        address = Address.objects.get(address_id=pk)
        address.delete()
        return JsonResponse("Deleted Successfully", safe=False)

    
@csrf_exempt
def contactApi(request):
    if request.method == 'GET':
        contacts = models.Contact.objects.all()
        contact_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contact_serializer.data, safe=False)
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(contact_id=contact_data['contact_id'])
        contact_serializer = ContactSerializer(
            contact_data, data=contact_data)
        if contact_data.is_valid():
            contact_data.save()
            return JsonResponse("Update Successfull", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        contact = Contact.objects.get(Address_Id=id)
        contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)


    
@csrf_exempt
def storagetypeApi(request):
    if request.method == 'GET':
        storageTypes = models.StorageType.objects.all()
        storageType_serializer = Storage_typeSerializer(storageTypes, many=True)
        return JsonResponse(storageType_serializer.data, safe=False)
    elif request.method=='POST':
        storageType_data =JSONParser().parse(request)
        storageType_serializer = Storage_typeSerializer(data=storageType_data)
        if storageType_serializer.is_valid():
            storageType_serializer.save()
            return JsonResponse("Added Successfull",safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        storageType_data = JSONParser().parse(request)
        storageType = StorageType.objects.get(storage_type_id=storageType_data['storage_type_id'])
        storageType_serializer = Storage_typeSerializer(
            storageType_data, data=storageType_data)
        if storageType_data.is_valid():
            storageType_data.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        storageType = StorageType.objects.get(Address_Id=id)
        storageType.delete()
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
    elif request.method=='DELETE':
        resourceType = ResourceType.objects.get(address_id=pk)
        resourceType.delete()
        return JsonResponse("Deleted Successfully", safe=False)

    
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
    elif request.method=='DELETE':
        resourceType = ResourceType.objects.get(address_id=pk)
        resourceType.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def accessLogApi(request):
    if request.method=='GET':
        accessLogs = AccessLog.objects.all()
        accessLog_serializer = access_logSerializer(accessLogs,many=True)
        return JsonResponse(accessLog_serializer.data,safe=False)
