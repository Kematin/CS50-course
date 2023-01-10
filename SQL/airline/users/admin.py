from django.contrib import admin
from .models import User

class UserView(admin.ModelAdmin):
    list_display = ("login", "password")    

# Register your models here.
admin.site.register(User, UserView)
