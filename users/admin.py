from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ()

    )