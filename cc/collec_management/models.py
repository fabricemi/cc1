from django.db import models
import datetime;
# Create your models here.
class Collec(models.Model):

    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    date=models.DateTimeField(default=datetime.date.today, null=False)

    def __str__(self):
        return self.title
