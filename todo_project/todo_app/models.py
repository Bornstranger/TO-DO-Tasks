from django.db import models

# Create your models here.
class Todo(models.Model):

    name = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
    