from rest_framework import serializers
from app.models import *
from emp.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ="__all__" 