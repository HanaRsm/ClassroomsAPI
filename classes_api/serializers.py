from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Classroom


class ClassesListSerializers(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		# feilds = [
		# # 'subject',
		# # 'year',
		# # 'teacher',
		# ]

		fields = '__all__'

class ClassesDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class ClassesCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'