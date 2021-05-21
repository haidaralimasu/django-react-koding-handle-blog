from django.contrib import admin
from blog.models import Post, BlogComment
from django_summernote.admin import SummernoteModelAdmin

class BlogPostAdmin(SummernoteModelAdmin):
  
    summernote_fields = ('content', )


admin.site.register((Post, BlogComment), BlogPostAdmin)
