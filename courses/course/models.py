from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length = 250)
	imgpath = models.CharField(max_length = 1000)

	def __str__(self):
		return self.name

class Branch(models.Model):
	latitude = models.CharField(max_length = 250)
	longitude = models.CharField(max_length = 250)
	address  = models.CharField(max_length = 250)

	def __str__(self):
		return self.address

class Contacts(models.Model):

	class ContactTypes(models.IntegerChoices):
		Phone = 1
		E_Mail = 2
		Facebook = 3

	type = models.IntegerField(choices=ContactTypes.choices)
	value = models.CharField(max_length=100)

	def __str__(self):
		return self.value

class Course(models.Model):
	name = models.CharField(max_length = 250)
	description = models.CharField(max_length = 1000)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	branches = models.ManyToManyField(Branch)
	contacts = models.ManyToManyField(Contacts)
	logo = models.CharField(max_length = 1000)

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name