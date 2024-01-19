
from rest_framework import serializers
from api.models import Company,Employee
# Create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
        # company id will reveal the id that is only read only
               company_id = serializers.ReadOnlyField()
               class Meta:
                       model=Company
                       fields="__all__"
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                        model=Employee
                        fields="__all__"