from rest_framework import generics as rest_views
from rest_framework import views as rest_base_views
from rest_framework.response import Response
from rest_framework import viewsets

from drf_demos.api.models import Employee, Department
from drf_demos.api.serializers import DepartmentSerializer, EmployeeSerializer, DemoSerializer


class DepartmentsListApiView(rest_views.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeesListApiView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        queryset = self.queryset

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset.all()


class DemoApiView(rest_base_views.APIView):
    def get(self, request):
        body = {
            'employees': Employee.objects.all(),
            'departments': Department.objects.all()
        }
        serializer = DemoSerializer(body)

        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
