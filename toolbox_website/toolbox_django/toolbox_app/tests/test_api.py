from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from ..models import *

class TestApi(APITestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'devweb2'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        #Client with basic auth credentials
        self.auth_client = APIClient()
        self.auth_client.login(username=self.username, password=self.password)
        
        #Client w/o basic auth credentials
        self.not_auth_client = APIClient()

        #Creating dummy objects 
        ##Person
        self.dummyPerson_dict = {
            "lastName": "foo",
            "firstName": "bar",
            "alias": "fobar",
            "birthDate": "1000-12-01",
            "email": "foo.bar@gmail.com",
            "pwd_test": "testpwd2"
        }
        self.dummyPerson_object = Persons.objects.create(**self.dummyPerson_dict)

    #######################
    ###   PERSONS API   ###

    def test_personsViewSet_list_GET(self):
        response = self.auth_client.get("/api/persons/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_personsViewSet_list_GET_noAuth(self):
        response = self.not_auth_client.get("/api/persons/", format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_personsViewSet_detail_GET(self):
        response = self.auth_client.get("/api/persons/1/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_personsViewSet_POST(self):
        data = {
            "lastName": "foo2",
            "firstName": "bar2",
            "alias": "fobar2",
            "birthDate": "1000-12-01",
            "email": "foo2.bar2@gmail.com",
            "pwd_test": "testpwd22"
        }
        response = self.auth_client.post("/api/persons/", data ,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_personsViewSet_aliases_GET(self):
        response = self.auth_client.get("/api/persons/aliases/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_personsViewSet_login_GET(self):
        #With correct email
        response = self.auth_client.get("/api/persons/login/?email=foo.bar@gmail.com", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)[0].get("email"), self.dummyPerson_dict.get("email"))
        self.assertEqual(json.loads(response.content)[0].get("pwd_test"), self.dummyPerson_dict.get("pwd_test"))
        
        #With incorrect email
        response = self.auth_client.get("/api/persons/login/?email=fakefoo.bar@gmail.com", format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(json.loads(response.content).get("error"), "no user with this email: fakefoo.bar@gmail.com")

    def test_personsViewSet_towns_GET(self):
        response = self.auth_client.get("/api/persons/1/towns/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_personsViewSet_tools_GET(self):
        response = self.auth_client.get("/api/persons/1/tools/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_personsViewSet_reviews_GET(self):
        response = self.auth_client.get("/api/persons/1/reviews/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_personsViewSet_groups_GET(self):
        response = self.auth_client.get("/api/persons/1/groups/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #######################
    ###    TOOLS API    ###

    ######################
    ###   GROUPS API   ###

    ######################
    ###   TOWNS  API   ###
    
    #######################
    ###  COUNTRIES API  ###