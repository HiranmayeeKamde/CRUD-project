from django.contrib import admin
from .models import UserProfile

# Decorators
@admin.register(UserProfile) # Decorator -> help to change the functionality of any class
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','password')