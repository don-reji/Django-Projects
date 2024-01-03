from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class TaskAPITestCase(TestCase):

    def test_list_tasks(self):
        response = self.client.get(reverse('tasks-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


