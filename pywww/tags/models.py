from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
   name = models.CharField(unique=True, max_length=100)
   slug = models.SlugField(unique=True, max_length=100)

   def save(self, *args, **kwargs):
      if not self.slug:
         n = self.name
         s = slugify(n)
         print(f'Autogeneracja sluga: {n} -> {s}')
         self.slug = s
      return super().save(*args, **kwargs)

   def __str__(self):
      return self.slug