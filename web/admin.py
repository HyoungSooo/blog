from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Project, Project_content

# Register your models here.

# Apply summernote to all TextField in model.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Super_User

# Register your models here.

admin.site.register(Super_User, UserAdmin)


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content')


admin.site.register(Post, SomeModelAdmin)
admin.site.register(Project, SomeModelAdmin)
admin.site.register(Project_content, SomeModelAdmin)
