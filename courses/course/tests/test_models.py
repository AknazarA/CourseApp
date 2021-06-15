from django.test import TestCase
from django.urls import reverse

from course.models import *

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Category.objects.create(name='Building', imgpath='somepath')

    def test_name(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_imgpath(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('imgpath').verbose_name
        self.assertEqual(field_label, 'imgpath')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)

    def test_imgpath_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('imgpath').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEqual(str(category), expected_object_name)



class BranchModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Branch.objects.create(latitude='74.85', longitude='84.85', address='Tokombaeva')

    def test_latitude(self):
        branch = Branch.objects.get(id=1)
        branch_latitude = branch._meta.get_field('latitude').verbose_name
        self.assertEqual(branch_latitude, 'latitude')

    def test_longtitude(self):
        branch = Branch.objects.get(id=1)
        branch_longtitude = branch._meta.get_field('longitude').verbose_name
        self.assertEqual(branch_longtitude, 'longitude')

    def test_address(self):
        branch = Branch.objects.get(id=1)
        branch_address = branch._meta.get_field('address').verbose_name
        self.assertEqual(branch_address, 'address')

    def test_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEqual(max_length, 250)

    def test_longtitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEqual(max_length, 250)

    def test_address_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEqual(max_length, 250)

    def test_object_name_is_address(self):
        branch = Branch.objects.get(id=1)
        expected_object_name = branch.address
        self.assertEqual(str(branch), expected_object_name)



class ContactsModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Contacts.objects.create(type=1, value='+996555001133')

    def test_type_in_contact_types(self):
    	contacts = Contacts.objects.get(id=1)
    	contacts_type = contacts.type
    	contacts_choices = contacts._meta.get_field('type').choices
    	self.assertTrue(contacts_type <= len(contacts_choices))

    def test_type(self):
        contacts = Contacts.objects.get(id=1)
        contacts_type = contacts._meta.get_field('type').verbose_name
        self.assertEqual(contacts_type, 'type')

    def test_value(self):
        contacts = Contacts.objects.get(id=1)
        contacts_value = contacts._meta.get_field('value').verbose_name
        self.assertEqual(contacts_value, 'value')

    def test_value_max_length(self):
        contacts = Contacts.objects.get(id=1)
        max_length = contacts._meta.get_field('value').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_contacts(self):
        contacts = Contacts.objects.get(id=1)
        expected_object_name = str(contacts.contactTypes[contacts.type - 1][1]) + ': ' + contacts.value
        self.assertEqual(str(contacts), expected_object_name)


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
    	category1 = Category.objects.create(name="Cooking", imgpath="somepath")
    	branch1 = Branch.objects.create(latitude="74.85",  longitude="84.54", address="Abdykadyrov")
    	contacts1 = Contacts.objects.create(type=1, value='+9960707070707')
    	contacts2 = Contacts.objects.create(type=2, value='a@f.com')

    	course = Course.objects.create(name='Кулинария Про', description='The best Cooking course ever', category=category1, logo='somelogo')
    	course.branches.add(branch1)
    	course.contacts.add(contacts1)
    	course.contacts.add(contacts2)

    def test_name(self):
    	course = Course.objects.get(id=1)
    	course_name = course._meta.get_field('name').verbose_name
    	self.assertEqual(course_name, 'name')

    def test_description(self):
        course = Course.objects.get(id=1)
        course_description = course._meta.get_field('description').verbose_name
        self.assertEqual(course_description, 'description')

    def test_logo(self):
        course = Course.objects.get(id=1)
        course_logo = course._meta.get_field('logo').verbose_name
        self.assertEqual(course_logo, 'logo')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)

    def test_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_logo_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('logo').max_length
        self.assertEqual(max_length, 1000)

    def test_category(self):
        course = Course.objects.get(id=1)
        category = Category.objects.get(id=1)

        self.assertEqual(category.name, course.category.name)

    def test_contancs_number(self):
    	course = Course.objects.get(id=1)
    	contacts_count = Contacts.objects.count()

    	self.assertEqual(contacts_count, course.contacts.count())

    def test_branch_number(self):
    	course = Course.objects.get(id=1)
    	branch_count = Branch.objects.count()

    	self.assertEqual(branch_count, course.branches.count())

    def test_course_name_is_name(self):
        course = Course.objects.get(id=1)
        expected_object_name = course.name
        self.assertEqual(str(course), expected_object_name)

    def test_get_absolute_url(self):
    	course = Course.objects.get(id=1)
    	self.assertEqual(course.get_absolute_url(), '/courses/1/')