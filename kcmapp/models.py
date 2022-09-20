from django.db import models

# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    name = models.CharField(max_length=10)

    
    def __str__ (self) :
        return self.title 