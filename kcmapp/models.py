from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True)

    def __str__ (self) :
        return self.title

    def clean(self):
        title = self.title
        if title == "":
            raise ValidationError("글을 작성해주세요")
        return super(Cashbook, self).clean()
