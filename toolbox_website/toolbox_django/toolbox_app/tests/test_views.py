from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

def test_index():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == status.HTTP_200_OK
    