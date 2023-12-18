from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
from django.utils import timezone
# Create your tests here.
class TaskAPITest(APITestCase): 

    # testing the tasks list endpoint
    def test_list_view(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if response.status_code==status.HTTP_404_NOT_FOUND:
            print('not found')
    