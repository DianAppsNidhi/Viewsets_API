from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Course, CourseSerializer
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet


# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




# class CourseViewset(viewsets.ViewSet):
#     def list(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many = True)
#         return Response(serializer.data)

   

#     def create(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)  
#         return Response(serializer.errors)    


#     def CourseRetrieve(self, request, pk ):
#         try:
#             course = Course.objects.get(pk=pk)
#         except  course.DoseNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)  

#         serializer = CourseSerializer(course)
#         return Response(serializer.data)


            

