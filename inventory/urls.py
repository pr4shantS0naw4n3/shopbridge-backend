from django.urls import path

from .views import InventoryDelete, InventoryGetAll, InventoryUpdate, InventoryGetOne, InventoryAdd
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="ShopBridge - Inventory Api",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
app_name = "users"
urlpatterns = [
    # Swagger Documentation URL
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='inventory-swagger-ui'),
    
    # Invetory API's
    path('inventory/add-item/', InventoryAdd.as_view()),
    path('inventory/get-items/', InventoryGetAll.as_view()),
    path('inventory/get-item/<int:pk>/', InventoryGetOne.as_view()),
    path('inventory/delete-item/<int:pk>/', InventoryDelete.as_view()),
    path('inventory/update-item/<int:pk>/', InventoryUpdate.as_view())
]