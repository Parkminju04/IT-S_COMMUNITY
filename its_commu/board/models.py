from django.db import models

# Create your models here.
class Announce(models.Model):
    doc_no = models.CharField(max_length=20, primary_key=True, null=False)
    writer = models.CharField(max_length=50, null=False)
    write_date = models.DateField(null=False)
    viewer = models.IntegerField(default=0, null=False)
    desc = models.CharField(max_length=255)
    insert_date = models.DateField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)
    insert_std = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.doc_no