from django.urls import path,include
from testapp.api import views
import json
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register('employees',views.Emplyee_ModelViewSet)
router.register('department',views.Department_ModelViewSet)

urlpatterns = [
    path('',include(router.urls))
]