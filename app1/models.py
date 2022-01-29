from django.db import models
from django.forms import CharField

class Book(models.Model):
  name = models.CharField(max_length=100)
  prize = models.IntegerField()
  pages = models.IntegerField()
  
  class Meta:
    ordering = ['-id']

  def __str__(self):
    return "{}".format(self.name)
