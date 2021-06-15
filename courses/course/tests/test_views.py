import json

from django.test import TestCase
from django.urls import reverse

from course.models import *
from course.views import *

class CourseListViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Create 5 courses
        number_of_courses = 5

        category1 = Category.objects.create(name="Cooking", imgpath="somepath")
        branch1 = Branch.objects.create(latitude="74.85",  longitude="84.54", address="Abdykadyrov")
        contacts1 = Contacts.objects.create(type=1, value='+9960707070707')
        contacts2 = Contacts.objects.create(type=2, value='a@f.com')

        for course_id in range(number_of_courses):
            course = Course.objects.create(
                name=f'Course {course_id}',
                description=f'Description {course_id}',
                category=category1,
                logo=f'somelogo {course_id}'
            )
            course.branches.add(branch1)
            course.contacts.add(contacts1)
            course.contacts.add(contacts2)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('http://127.0.0.1:8000/courses/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
"""
    def test_view_post(self):
        post = {
		    "name": "New Course",
		    "description": "New Description",
		    "category": 1,
		    "branches": [
		        {
		            "latitude": "00.11",
		            "longitude": "11.00",
		            "address": "New address"
		        }
		    ],
		    "logo": "somelogo",
		    "contacts":[
		        {
		            "type": 1,
		            "value": "0707070707"
		        },
		        {
		            "type": 2,
		            "value": "b@f.com"
		        }
		    ],
		    "logo": "somelogo"
		}

        response = self.client.post(reverse('courses'), post)
        self.assertEquals(response.status_code, 201)
        data = json.loads(response.content)

        content = {
		    "name": "New Course",
		    "description": "New Description",
		    "category": 1,
		    "branches": [
		        {
		            "latitude": "00.11",
		            "longitude": "11.00",
		            "address": "New address"
		        }
		    ],
		    "contacts":[
		        {
		            "type": 1,
		            "value": "0707070707"
		        },
		        {
		            "type": 2,
		            "value": "b@f.com"
		        }
		    ],
		    "logo": "somelogo"
		}
        self.assertEquals(data, content)
"""

class CourseDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Create 5 courses
        number_of_courses = 5

        category1 = Category.objects.create(name="Cooking", imgpath="somepath")
        branch1 = Branch.objects.create(latitude="74.85",  longitude="84.54", address="Abdykadyrov")
        contacts1 = Contacts.objects.create(type=1, value='+9960707070707')
        contacts2 = Contacts.objects.create(type=2, value='a@f.com')

        for course_id in range(number_of_courses):
            course = Course.objects.create(
                name=f'Course {course_id}',
                description=f'Description {course_id}',
                category=category1,
                logo=f'somelogo {course_id}'
            )
            course.branches.add(branch1)
            course.contacts.add(contacts1)
            course.contacts.add(contacts2)

    def test_detail_view_url_exists_at_desired_location(self):
        response = self.client.get('http://127.0.0.1:8000/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_url_accessible_by_name(self):
        response = self.client.get(reverse('detail', args=[1]))
        self.assertEqual(response.status_code, 200)