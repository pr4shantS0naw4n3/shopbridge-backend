from django.db import models

# Inventory model to store item data
class Inventory(models.Model):
    item_name = models.CharField(max_length=128,blank=False, null=False, unique=True)
    item_price = models.IntegerField(default=0)
    description = models.TextField(blank=False, null=False)
    item_quantity = models.IntegerField(default=0)
    item_sold = models.IntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def to_json(self):
        data = {
            "id": self.id,
            "item_name": self.item_name,
        }
        return data
    
    def get_json(self):
        data = {
            "id": self.id,
            "item_name": self.item_name,
            "item_price": self.item_price,
            "description": self.description,
            "item_quantity": self.item_quantity,
            "item_sold": self.item_sold,
            "item_added_on": self.added_on,
            "item_updated_on": self.updated_on
        }
        return data
