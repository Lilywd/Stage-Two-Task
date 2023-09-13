from django.db import models

# Create your models here.
class Person(models.Model):
    
    name = models.CharField(max_length=100)
   

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name