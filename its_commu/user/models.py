from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=20, null=False)
    pw = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=50, null=False, unique=True)
    std_id = models.CharField(max_length=20, primary_key=True, null=False)
    birth = models.DateField(null=False)
    tel = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    github = models.CharField(max_length=50)
    in_date = models.DateField(null=False)
    type = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    insert_date = models.DateField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.id
