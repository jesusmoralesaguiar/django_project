from django.test import TestCase
from testdb.models import Cities


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_createCity(self):
        my_model = Cities.objects.create(name='Guia de Isora', country='Spain', population=20000, area=143)
        self.assertEqual(my_model.name, "Guia de Isora")

    def test_home_page_status_code(self):
        response = self.client.get('/productbydiscipline')
        self.assertEqual(response.status_code, 200)
