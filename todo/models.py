from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) 
    done = models.BooleanField(null=False,  blank=False, default=False)

    def __str__(self):
      return self.name

# # todo/models.py

# from django.db import models

# class TodoItem(models.Model):
#     name = models.CharField(max_length=255)
#     done = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name
