from django.contrib import admin
from .models import Project, Tag, Message


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Message)

