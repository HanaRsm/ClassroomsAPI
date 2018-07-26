from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from classes.models import Classroom
from .serializers import ClassesListSerializers, ClassesDetailSerializer, ClassesCreateUpdateSerializer
# Create your views here.

class ClassesListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassesListSerializers
	

class ClassesDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassesDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassesCreateView(CreateAPIView):
	serializer_class = ClassesCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class ClassesUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassesCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassesDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassesListSerializers
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'