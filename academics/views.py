
from rest_framework.viewsets import ModelViewSet

from academics.models import Course, AcademicSession
from academics.serializers import CourseSerializer, AcademicSessionSerializer


# Create your views here.

class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_context(self):
        return {"department_id": self.kwargs.get("nested_1_pk")}


class AcademicViewSet(ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer

