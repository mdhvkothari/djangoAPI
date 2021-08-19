from django.contrib import admin
from django.urls import path,include
from API import views
from rest_framework.routers import DefaultRouter



#make an object
router = DefaultRouter()

#register views function with router
router.register('studentapi',views.StudentViewSet,basename= 'student')
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename = 'student')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]
