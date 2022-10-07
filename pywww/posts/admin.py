from django.contrib import admin
from posts.models import Post
from import_export import resources
from import_export.admin import ExportMixin


# Register your models here.
class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "title", "created", "modified", "published"]
    search_fields = ["title", "content"]
    list_filter = ["published", 'created', 'modified']
    resource_class = PostResource

admin.site.register(Post, PostAdmin)
