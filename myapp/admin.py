from django.contrib import admin
from .models import Post, Profile,BlogComment,Following

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display =['id','title','description','author','posted_date']

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['user','status','qualification','profession','image','about','follower','following']


@admin.register(BlogComment)
class AdminBlogComment(admin.ModelAdmin):
    list_display = ['id','user','post','comment','timestamp']

admin.site.register(Following)