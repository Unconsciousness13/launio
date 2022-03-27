from django.contrib import admin

# Register your models here.
from launio.club import models


@admin.register(models.Gymnast)
class GymnastAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('first_name', 'last_name'), }
    pass
