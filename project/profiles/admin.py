from django.contrib import admin

from profiles.models import DetailProfile


class AdminProfile(admin.ModelAdmin):
    model = DetailProfile
    list_display = ('first_name', 'last_name', 'birthday', 'created_at')


admin.site.register(DetailProfile, AdminProfile)
