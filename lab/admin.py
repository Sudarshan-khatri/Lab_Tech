from django.contrib import admin
from .models  import LabModel


class LabmodelAdmin(admin.ModelAdmin):
    readonly_fields=('lab_code',)


# Register your models here.
admin.site.register(LabModel,LabmodelAdmin)
