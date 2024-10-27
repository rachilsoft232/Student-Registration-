from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def _str_(self):
        return self.name