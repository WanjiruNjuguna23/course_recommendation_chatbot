from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Course, Interest

# Test the Course model
class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Math 101', description='Introduction to Math')

    def test_course_creation(self):
        self.assertEqual(self.course.name, 'Math 101')
        self.assertEqual(self.course.description, 'Introduction to Math')

# Test the Interest model
class InterestModelTest(TestCase):
    def setUp(self):
        self.interest = Interest.objects.create(name='Math')

    def test_interest_creation(self):
        self.assertEqual(self.interest.name, 'Math')

# Test the select_interests view
class SelectInterestsViewTest(TestCase):
    def test_select_interests_view_status_code(self):
        response = self.client.get(reverse('select_interests'))
        self.assertEqual(response.status_code, 200)

# Test the recommend_courses view
class RecommendCoursesViewTest(TestCase):
    def test_recommend_courses_view_status_code(self):
        response = self.client.post(reverse('recommend_courses'), {'interests': []})
        self.assertEqual(response.status_code, 200)

