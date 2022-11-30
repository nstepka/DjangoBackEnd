# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbcResource(models.Model):
    abc_resource_id = models.AutoField(primary_key=True)
    inventory_id = models.IntegerField()
    resource_type_id = models.IntegerField()
    resource_name = models.CharField(max_length=45)
    max_number_of_resources = models.BigIntegerField()
    current_number_of_resources = models.BigIntegerField()
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abc_resource'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    abc_client_id = models.IntegerField()
    inventory_name = models.CharField(max_length=45)
    storage_type_id = models.IntegerField()
    max_item_capacity = models.BigIntegerField()
    address_id = models.IntegerField(null=True)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'

class ResourceType(models.Model):
    resource_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resource_type'

class InventoryDDL(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    inventory_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'InventoryDDL'

