from django.db import models

# Create your models here.
class It_plan(models.Model):
    date = models.DateField(primary_key=True)
    schedule = models.CharField(max_length=100)
    insert_date = models.DateField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.date