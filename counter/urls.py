from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JarCountViewSet, update_jar_count

router = DefaultRouter()
router.register(r'jarcounts', JarCountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update_jar_count/', update_jar_count, name='update_jar_count'),
]
