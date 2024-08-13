from django.db import models


# Create your models here.
class Comp(models.Model):
    doc_no = models.IntegerField(primary_key=True, null=False)
    writer = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    viewer = models.IntegerField(null=False, default=0)
    write_date = models.DateTimeField(null=False)
    reply_count = models.IntegerField(null=False, default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.doc_no
