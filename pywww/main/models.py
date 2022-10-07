from django.db import models

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
   bio = models.TextField()

   def __str__(self):
      return f'Profile for {self.user} : {self.bio[:30]}...'