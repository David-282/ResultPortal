

from django.urls import path, include
from .views import CourseView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', CourseView, basename='courses')




urlpatterns = [
    path("", include(router.urls)),

]