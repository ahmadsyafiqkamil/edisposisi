from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.models import User,ProfileUser
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = get_user_model()


admin.site.register(User,UserAdmin)
admin.site.register(ProfileUser)
