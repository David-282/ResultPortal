#
#
from django.urls import path, include
from rest_framework import routers

from .views import AcademicViewSet

router = routers.DefaultRouter()
router.register('academic_session', AcademicViewSet, basename='academic_session')



urlpatterns = [
    path("", include(router.urls)),
]