from django.db import models


# Create your models here.
class Comment(models.Model):
    reply_no = models.IntegerField(primary_key=True, null=False)
    writer = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    date = models.DateTimeField
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    type = models.CharField(max_length=10, null=False)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.reply_no
