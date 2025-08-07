from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        info : str = f'{self.name}, {self.age}'
        return info 