from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser





class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    #allow all register users
    permission_classes = [IsAuthenticated]
    #allow all all      
    # permission_classes = [AllowAny]
    #allow only those user who have staff tick 
    # permission_classes = [IsAdminUser]

