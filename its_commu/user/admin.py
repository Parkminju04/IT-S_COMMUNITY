from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
class UserAdmin(admin.ModelAdmin) :
    list_display = ('id', 'username', 'std_id', 'birth', 'tel', 'email', 'github')
    exclude = ('password',)

