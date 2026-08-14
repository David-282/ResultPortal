# from django.core.exceptions import ValidationError
# from loguru import logger
#
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
#
# from core.models import Department
# from core.serializers import DepartmentSerializer
#
#
# # Create your views here.
# @api_view(['POST'])
# def create_department(request):
#     try:
#         serializer = DepartmentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = serializer.validated_data['name']
#         code = serializer.validated_data['department_code']
#         logger.info(f"data validate for department {name}")
#
#
#         if Department.objects.filter(department_code=code).exists():
#             logger.info(f"Department with code {code} already exists")
#             return Response({"message": "department already exists"}, status=status.HTTP_400_BAD_REQUEST)
#
#         Department.objects.create(**serializer.validated_data)
#
#         # serializer.save()
#         logger.info(f"department {name} created")
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         logger.error(f"Error creating department {str(e)}")
#         return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
#
# @api_view(['GET'])
# def get_department(request,department_code):
#     department = get_object_or_404(Department, department_code=department_code, is_active=True)
#     serializer = DepartmentSerializer(department)
#     logger.info(f"department {department_code} retrieved successfully")
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['PUT', 'PATCH'])
# def update_department(request, department_code):
#     department = get_object_or_404(Department, department_code=department_code, is_active=True)
#
#     try:
#         serializer = DepartmentSerializer(department, data=request.data, partial=request.method == 'PATCH')
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         logger.info(f"department {department_code} updated successfully")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except ValidationError as e:
#         logger.error(f"Error validating department {str(e)}")
#         return Response("Error validating department", status.HTTP_500_INTERNAL_SERVER_ERROR)
#     except Exception as e:
#         logger.error(f"Error updating department {str(e)}")
#         return Response("Error updating department", status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
#
# @api_view(['DELETE'])
# def delete_department(request, department_code):
#     department = get_object_or_404(Department, department_code=department_code)
#     department.is_active = False
#     department.save()
#     logger.info(f"department {department_code} deleted successfully")
#     return Response(status=status.HTTP_204_NO_CONTENT)
# # @api_view(['GET'])
# # def get_department(code):
# #     try:
# #         department = Department.objects.filter(code=code)
# #         serializer = DepartmentSerializer(department)
# #         logger.info(f"Department found")
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #
# #     except Exception as e:
# #         logger.error(f"Error getting department {str(e)}")
# #         return Response({"message": f"Department with code {code} not found"},status=status.HTTP_404_NOT_FOUND)
# #
# # @api_view(['GET'])
# # def get_department(request, code):
# #
# #
# #
# # @api_view(['DELETE'])
# # def delete_department(code):
# #     try:
# #         department = Department.objects.get(code=code)
# #         name = department.name
# #         department.delete()
# #         logger.info(f"Department '{name}' deleted")
# #         return Response({"message": f"Department '{name}' deleted successfully"}, status=status.HTTP_200_OK)
# #
# #     except Department.DoesNotExist:
# #         logger.error(f"Department with code {code} not found")
# #         return Response({"message": f"Department with code {code} not found"}, status=status.HTTP_404_NOT_FOUND)
# #     except Exception as e:
# #         logger.error(f"Error deleting department: {str(e)}")
# #         return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# #
# #
# # @api_view(['PUT', 'PATCH'])
# # def update_department(request, department_id):
# #     try:
# #         department = Department.objects.get(id=department_id)
# #         serializer = DepartmentSerializer(data=request.data, partial=True)
# #         serializer.is_valid(raise_exception=True)
# #         code = serializer.validated_data['code']
# #
# #         if code:
# #             existing_department = (Department.objects.filter(code=code).exclude(id=department_id))
# #
# #             if existing_department.exists():
# #                 logger.error(f"department with code {code} already exists")
# #                 return Response({"message": "department with code already exists"},
# #                                 status=status.HTTP_400_BAD_REQUEST)
# #
# #         for key, value in serializer.validated_data.items():
# #             setattr(department, key, value)
# #
# #         department.save()
# #
# #         logger.info(f"department {department.name} updated")
# #
# #         return Response({"message": "department updated successfully",
# #                          "data": {
# #                              "id": department.id,
# #                              "name": department.name,
# #                              "code": department.code,
# #                              "description": department.description,
# #                          }
# #                          }, status=status.HTTP_200_OK)
# #     except Department.DoesNotExist:
# #         logger.error(
# #             f"department with id {department_id} does not exist"
# #         )
# #         return Response({"message": "department not found"}, status=status.HTTP_404_NOT_FOUND)
# #     except Exception as e:
# #         logger.error(f"Error updating department: {str(e)}")
# #         return Response({"message": "Error updating department"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
#
#     # Department.objects.create(
#     #     name = serializer.validated_data['name'],
#     #     code = serializer.validated_data['code'],
#     #     description = serializer.validated_data['description'],
#     # ) another style
#
#     # return Response(serializer.data, )
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from core.models import Department
from core.serializers import DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return [IsAuthenticated()]
        return [AllowAny(),]