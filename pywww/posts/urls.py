from django.urls import path
from posts.views import posts_list, posts_details, add_post_form, toggle_sponsored
app_name = "posts"
urlpatterns = [
   path('', posts_list, name='list'),
   path('<int:id>', posts_details, name='details'),
   path('add', add_post_form, name='add'),
   path('toggle_sponsored', toggle_sponsored, name='toggle_sponsored')
]
