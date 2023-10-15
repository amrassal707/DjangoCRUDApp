from django.test import TestCase
from django.test import Client
# Create your tests here.

from .models import student
# Create your tests here.

class testCasesForModel(TestCase):
    
    
    @classmethod
    def setUpTestData(cls):
        client = Client()
        cls.students= student.objects.create(name = 'ahmed' , age  = 10 )
    def testFields(self):
        self.assertIsInstance(self.students.name, str)
        self.assertIsInstance(self.students.age, int)
    def testReadingData(self):
        response= self.client.get('http://127.0.0.1:8000/readallstudents/') 
        #assert response.status_code == 200
        self.assertEqual(student.objects.count(),1)
    def addnewData(self):
        response=self.client.post('http://127.0.0.1:8000/addstudent/?name=amr&age=18')
        self.assertEqual(student.objects.count(), 2)
    def deleteData(self):
        response= self.client.delete('http://127.0.0.1:8000/delete/1')
        self.assertEqual(student.objects.count(), 0)
    
        
        
        