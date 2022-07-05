from django.urls import path
from .views import create_db, CouchViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('createdb/', create_db)
]

router = DefaultRouter()

router.register(r'stats', CouchViewSet)
urlpatterns += router.urls
