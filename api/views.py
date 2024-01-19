from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
               queryset = Company.objects.all()
               serializer_class= CompanySerializer
               @action(detail=True,methods=['get'])
               def employees(self,request,pk=None):
                 try: 
                   company = Company.objects.get(pk=pk)
                   emps = Employee.objects.filter(company=company)
                   emps_serializers = EmployeeSerializer(emps,many=True,context={"request":request})
                   
                   print("get employees of ",pk, "Compnaies")
                   return Response(emps_serializers.data)
                 except Exception as e:
                   return Response({
                          "message":"Company might not exists"
                   })
                             
class EmployeeViewSEt(viewsets.ModelViewSet):
               queryset = Employee.objects.all()
               serializer_class= EmployeeSerializer               