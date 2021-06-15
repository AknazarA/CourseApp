from rest_framework import serializers
from .models import Course, Branch, Contacts, Category

class CategorySerializer(serializers.ModelSerializer):
	class  Meta:
		model = Category
		fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):

	class Meta:
		model = Branch
		fields = ['latitude', 'longitude', 'address']

class ContanctsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contacts
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	contacts = ContanctsSerializer(many=True)
	branches = BranchSerializer(many=True)
	#category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())

	class Meta:
		model = Course
		fields = '__all__'

	def create(self, validated_data):
		branches_data = validated_data.pop('branches')
		contacts_data = validated_data.pop('contacts')


		course = Course.objects.create(**validated_data)

		for branch_data in branches_data:
			branch = Branch.objects.create(course=course, **branch_data)
			course.branches.add(branch)

		for contact_data in contacts_data:
			contact = Contacts.objects.create(course=course, **contact_data)
			course.contacts.add(contact)

		return course