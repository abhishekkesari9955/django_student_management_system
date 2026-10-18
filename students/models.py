from django.db import models

# Create your models here.
 
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.full_name