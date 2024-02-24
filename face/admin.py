from django.contrib import admin
from face.models import UserSign
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','Name','Email','Mobile','Password']
admin.site.register(UserSign,UserAdmin)
