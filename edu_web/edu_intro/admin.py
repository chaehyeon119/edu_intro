from django.contrib import admin
from .models import intro, Student
from embed_video.admin import AdminVideoMixin
# Register your models here.

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video')

admin.site.register(intro, PostAdmin)
admin.site.register(Student) 