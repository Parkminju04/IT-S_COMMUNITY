from django.db import models

# Create your models here.
class It_prj(models.Model):
    prj_no = models.IntegerField(primary_key=True, null=False)
    member = models.CharField(max_length=255, null=False)
    team = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    intro = models.TextField
    keyword = models.CharField(max_length=50)
    viewer = models.IntegerField(null=False, default=0)
    date = models.DateTimeField
    img = models.CharField(max_length=50)
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.prj_no