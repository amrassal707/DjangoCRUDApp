from django.db import models

# Create your models here.

class student(models.Model):
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.name + ":" + str(self.age)
    
    