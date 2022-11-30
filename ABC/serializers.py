from rest_framework import serializers

from api.models import ( AbcResource,  Inventory, ResourceType, InventoryDDL)


class Inventory_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('inventory_id', 'abc_client_id', 'inventory_name', 'storage_type_id', 'max_item_capacity', 'address_id', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')


class Resource_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = ('resource_type_id', 'type_name', 'created_by',
                 'created_date', 'modified_by', 'modified_date', 'is_deleted')


class Abc_resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbcResource
        fields = ('abc_resource_id', 'inventory_id', 'resource_type_id', 'resource_name', 'max_number_of_resources', 'current_number_of_resources', 'created_by', 'created_date',
                 'modified_by', 'modified_date', 'is_deleted')

class InventoryDDL_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryDDL
        fields = ('inventory_id', 'inventory_name')
