from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
 list_display = ['username', 'first_name', 'last_name', 'is_active', 
                   'date_joined', 'email', 'phone', 'profile_pic', 'file', 'Reg_id']