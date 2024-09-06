from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    responsable = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

