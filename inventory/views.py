from functools import partial
from .models import Inventory
from .serializer import InventorySerializer

from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

# GET API - Get record of all inventory items
class InventoryGetAll(APIView):
    @swagger_auto_schema(responses={200: InventorySerializer(many=True)},operation_description="Lists the items in the inventory.")
    def get(self, request):
        try:
            inventory_obj = Inventory.objects.all()
            serializer = InventorySerializer(inventory_obj, many=True)
            response = {
                "data":serializer.data
            }
            return Response(response)
        except Exception as e:
            raise APIException(str(e))

# GET API - Get record of single inventory items by ID
class InventoryGetOne(APIView):
    @swagger_auto_schema(responses={200: InventorySerializer()},operation_description="Get single item of the provided item id from the inventory.")
    def get(self, request, pk):
        try:
            item = Inventory.objects.get(pk=pk)
            response = {
                "data":item.get_json()
            }
            return Response(response,status=status.HTTP_204_NO_CONTENT)
        except Inventory.DoesNotExist:
            return Response({"message":"Data not found."},status=status.HTTP_404_NOT_FOUND)

# POST API - Add new item to the inventory
class InventoryAdd(APIView):
    @swagger_auto_schema(request_body=InventorySerializer,operation_description="Adds new item to the inventory.")
    def post(self, request):
        try:
            serializer = InventorySerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                response = {
                    "status":200,
                    "messgae":"Item added to the inventory successfully"
                }
                return Response(response, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise APIException(str(e))

# DELETE API - Delete record from inventory by ID
class InventoryDelete(APIView):
    @swagger_auto_schema(operation_description="Deletes item of the provided item id from the inventory.")
    def delete(self,request,pk):
        try:
            item = Inventory.objects.get(pk=pk)
            response = {
                "message": "Item deleted from inventory successfully",
                "data":item.to_json()
            }
            item.delete()
            return Response(response,status=status.HTTP_204_NO_CONTENT)
        except Inventory.DoesNotExist:
            return Response({"message":"Data not found."},status=status.HTTP_404_NOT_FOUND)

# DELETE API - PUT, PATCH - Update entire or specific fields of record by ID
class InventoryUpdate(APIView):
    @swagger_auto_schema(request_body=InventorySerializer,operation_description="Modify entire record of the provided item id from the inventory.")
    def put(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            validate_request = InventorySerializer(inventory, data=request.data)
            if(validate_request.is_valid()):
                validate_request.save()
                response = {
                    "message": "Item updated successfully",
                    "updated_data": validate_request.data
                }
                return Response(response,status = status.HTTP_200_OK)

            return Response(validate_request.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise APIException(str(e))
    
    @swagger_auto_schema(request_body=InventorySerializer,operation_description="Modify fields of record of the provided item id from the inventory.")
    def patch(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            validate_request = InventorySerializer(inventory, data=request.data, partial=True)
            if(validate_request.is_valid()):
                validate_request.save()
                response = {
                    "message": "Item updated successfully",
                    "updated_data": validate_request.data
                }
                return Response(response,status = status.HTTP_200_OK)

            return Response(validate_request.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise APIException(str(e))
