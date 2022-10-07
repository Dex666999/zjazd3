from django.db import models
from django.utils.timezone import now, timedelta


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        """Check if created is older than now() - n days"""
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Post(Timestamped):
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=255)  # pole tekstowe o określonej długości
    content = models.TextField()  # pole tekstowe o nieokreślonej długości
    published = models.BooleanField(default=False)  # flaga true/false
    created = models.DateTimeField(auto_now_add=True)  # data utworzenia - tylko przy utworzeniu
    modified = models.DateTimeField(auto_now=True)  # data modyfikacji - zawsze gdy klikniemy save
    tags = models.ManyToManyField('tags.Tag', related_name="posts")
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    sponsored = models.BooleanField(default=False)


    def is_content_long(self, n_chars=200):
        # napisać metode modelu odpowiadającą na pytanie czy post jest długi.
        # długie posty w szablonie szczgółów skracamy do 200 znaków i dodajemy ...
        return len(self.content) > n_chars

    def short_content(self, n=200):
        return self.content[:n]

    def __str__(self):
        return f'{self.title} by {self.author}'
