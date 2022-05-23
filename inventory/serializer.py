from json import loads
from json.decoder import JSONDecodeError
from django.core.exceptions import ValidationError
from .models import Inventory
from rest_framework import serializers

# Validate item name
def item_name(value):
    try:
        value = int(value)
    except:
        pass

    if isinstance(value,int):
        raise ValidationError('Please enter a valid item name.')

# Validate integer fields (item_price and item quntity)
def validate_integer_field(value):
    if(value <= 0):
        raise ValidationError('Please enter a valid integer value greater than zero.')

# Inventory serilizer to validate the data and convert it to json readable format
class InventorySerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(required=True, validators=[item_name])
    item_price = serializers.IntegerField(required=True, validators=[validate_integer_field])
    description = serializers.CharField(required=True)
    item_quantity = serializers.IntegerField(required=True, validators=[validate_integer_field])

    class Meta:
        model = Inventory
        fields = ['id','item_name','item_price','description','item_quantity','item_sold','added_on','updated_on']
