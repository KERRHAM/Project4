from django.contrib import admin
from .models import About, Post_request
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(Post_request)
class Post_requestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)