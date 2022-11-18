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
def contactApi(request):
    if request.method == 'GET':
        contacts = models.Contact.objects.all()
        addresses_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(addresses_serializer.data, safe=False)
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to Add address", safe=False)
    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(Address_Id=contact_data['contact_id'])
        contact_serializer = ContactSerializer(
            contact_data, data=contact_data)
        if contact_data.is_valid():
            contact_data.save()
            return JsonResponse("Added Successfull", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        contact = Contact.objects.get(Address_Id=id)
        contact.delete()
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




