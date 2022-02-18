import datetime
from urllib import response
from django.test import TestCase

# Create your tests here.
from .models  import Favorito
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
class BookmarkModelTest(TestCase):

  def test_create_favorito(self):
    user1 = User.objects.create_user(username="admin",password="admin")
    bk = Favorito()
    bk.titulo = "GOOGLE"
    bk.url = "hhtps//www.google.com.pe"
    bk.fecha_registro = timezone.now()
    bk.save()

    self.assertEqual(bk.titulo,"GOOGLE")
    # self.assertEqual(bk.fecha_registro,timezone.now())

class BookmarkApiViewTests(APITestCase):
  def test_bookmark_post(self):

    user1 = User.objects.create_user(username='admin',password='admin')
    url = reverse('app:favorito')
    data = {
      'titulo':'nuevo bookmark',
      'url':'https://www.google.com',
      'user':'1'
    }

    response = self.client.post(url,data,format='json')
    self.assertEqual(response.status_code,200)
    self.assertEqual(Favorito.objects.count(),1)
    self.assertEqual(Favorito.objects.get().titulo,'nuevo bookmark')

# Para ejecutar los test se corre el código:
# python3 manage.py test api