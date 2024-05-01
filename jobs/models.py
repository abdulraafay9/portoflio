from django.db import models

# Create your models here.

class Job(models.Model):
    Summary1=models.CharField(max_length=3000)
    Summary2=models.CharField(max_length=2000)


    def __str__(self):
        return self.Summary1 
