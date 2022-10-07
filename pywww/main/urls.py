from django.urls import path
from main.views import hello_world, contact_us

app_name = 'main'
urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('contact_us', contact_us, name='contact_us'),
]
