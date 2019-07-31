from django.db import models


class Name(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name 
    

class Person(models.Model):
    name = models.ForeignKey(Name , on_delete=models.CASCADE)
    age = models.IntegerField(default=12)

    def __str__(self):
        return self.name.first_name


    
