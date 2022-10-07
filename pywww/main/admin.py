from django.contrib import admin
from main.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    ...

admin.site.register(UserProfile, UserProfileAdmin)