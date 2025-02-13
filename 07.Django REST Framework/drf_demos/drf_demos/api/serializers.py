from rest_framework import serializers


from drf_demos.api.models import Employee, Department


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')


class ShortDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    employee_set = ShortEmployeeSerializer(many=True)
    class Meta:
        model = Department
        fields = '__all__'

def get_or_create_department_by_name(department_name):
    try:
        return Department.objects.filter(name=department_name).get()
    except Department.DoesNotExist:
        return Department.objects.create(name=department_name)


class EmployeeSerializer(serializers.ModelSerializer):
    department = ShortDepartmentSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        department_name = validated_data.pop('department').get('name')


        return Employee.objects.create(**validated_data, department=get_or_create_department_by_name(department_name))



class DemoSerializer(serializers.Serializer):
    employees = ShortEmployeeSerializer(many=True)
    departments = ShortDepartmentSerializer(many=True)
