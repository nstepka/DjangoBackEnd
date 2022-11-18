from rest_framework import serializers

from ABCAPP.models import (AbcClient, AbcResource, AccessLog, Address,
                           ClientContacts, Contact, Inventory, ResourceType,
                           StorageType)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields=('address_id','state','address_line_1','address_line_2','country','postal_code','city',
         'created_by', 'modified_by', 'created_date', 'modified_by', 'modified_date', 'is_deleted')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_id', 'email_address', 'phone_number', 'first_name', 'last_name', 'middle_name', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')


class Abc_clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbcClient
        fields = ('abc_client_id', 'client_name', 'company_address_id', 'phone_number', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')


class Storage_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        field = ('storage_type_id', 'type_name', 'created_by', 'created_date', 'modified_by', 'modified_date', 'is_deleted')


class Inventory_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        field = ('inventory_id', 'abc_client_id', 'inventory_name', 'storage_type_id', 'max_item_capacity', 'address', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')


class Resource_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        field = ('resource_type_id', 'type_name', 'created_by',
                 'created_date', 'modified_by', 'modified_date', 'is_deleted')


class Abc_resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbcResource
        field = ('abc_resource_id', 'inventory_id', 'resource_type_id', 'resource_name', 'max_number_of_resources', 'current_number_of_resources', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')


class access_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        field = ('access_log_id', 'username', 'resource_type_id', 'action', 'table_name', 'field_name', 'screen_name', 'created_date')
