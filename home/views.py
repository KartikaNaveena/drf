from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializers import PeopleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['GET', 'POST'])
def index(request):
    courses = {
          'course_name': 'python',
          'learn' : [ 'flask' , 'Django' ,'tornado'],
          'course_provider' : 'Scaler'
              }
    if request.method == 'GET' :
        return Response(courses)
    elif request.method == 'POST' :
        data=request.data
        print('**')
        print(data)
        return Response(courses)


    
class PeopleViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PeopleSerializer
    queryset = Person.objects.all() 
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id= data["id"])
        serializer = PeopleSerializer(obj ,data = data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
  
   