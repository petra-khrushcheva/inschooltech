from config.basemodels import BaseAdminModel
from django.contrib import admin

from .models import Lab, Test


class LabAdmin(BaseAdminModel):
    list_display = ('name', 'id')
    search_fields = ('name',)


class TestAdmin(BaseAdminModel):
    list_display = ('id', 'lab_id')


admin.site.register(Lab, LabAdmin)
admin.site.register(Test, TestAdmin)
