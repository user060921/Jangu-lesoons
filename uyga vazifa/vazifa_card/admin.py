from django.contrib import admin
from . models import sifat
admin.site.site_header='Bizning website | It-school'
admin.site.site_title='E-commercial website'
class StudentAdmin(admin.ModelAdmin):
    list_display=['user',]
    list_filter=['title',]
    search_fields=['narxi',]
    list_editable=['description',]
admin.site.register(sifat)

