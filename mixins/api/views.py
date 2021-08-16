from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



class student_api(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    

class studentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class studentRetrieve(GenericAPIView,RetrieveModelMixin):
    #we don't have to pass id it will automatically fetch form the url and gives particular data
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class studentUpdate(GenericAPIView,UpdateModelMixin):
    #we don't have to pass id it will automatically fetch form the url and gives particular data
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class studentDelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



#if we want to make them in a one class we have to categorise into 2 group
#one is in which pk is not required like in createMixin and retrieveMixin
#and other in which PK is required rest all 



# class student_api(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class studentRetrieve(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     #we don't have to pass id it will automatically fetch form the url and gives particular data
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

