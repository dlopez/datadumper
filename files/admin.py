from django.contrib import admin

from files.models import File


class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('uploaded_at', )
    list_display = ('__str__', 'uploaded_at')


admin.site.register(File, FileAdmin)

