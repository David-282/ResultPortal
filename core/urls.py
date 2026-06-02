# from django.urls import path
#
# from .views import create_department, get_department, delete_department, update_department
# from rest_framework_nested import routers
#
# urlpatterns = [
#     path('create_department/', create_department, name='create_department'),
#     path('get_department/<str:department_code>/', get_department, name='get_department'),
#     path('delete_department/<str:department_code>/', delete_department, name='delete_department'),
#     path('update_department/<str:department_code>/',update_department, name = 'update_department')
# ]


from django.urls import include, path
from academics.views import CourseView
from .views import DepartmentViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
dept_router = routers.NestedDefaultRouter(router, 'departments')
dept_router.register('course', CourseView, basename='course')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(dept_router.urls)),
]