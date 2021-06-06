from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseList(APIView):
	serializer_class = CourseSerializer

	def get(self, request, *args, **kwargs):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
	serializer_class = CourseSerializer

	def get(self, request, pk):
		course = Course.objects.filter(id=pk)
		serializer = CourseSerializer(course, many=True)
		return Response(serializer.data)

	def delete(self, request, pk):
		course = Course.objects.filter(id=pk)
		course.delete()

		return Response("Course is deleted")