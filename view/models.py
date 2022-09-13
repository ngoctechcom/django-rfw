from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.model + ' - ' + self.name
