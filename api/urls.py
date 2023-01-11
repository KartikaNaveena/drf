from home.views import index
from home.views import PeopleViewSet
from django.urls import path , include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns= router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
]