from django.contrib import admin
from news.models import Post,Student,ContactUs
# Register your models here.
admin.site.site_header='Bizning website | It-school'
admin.site.site_title='E-commercial website'
class StudentAdmin(admin.ModelAdmin):
    list_display=['fullname','roll_no','email','phone','fee']
    list_filter=['fullname','roll_no']
    search_fields=['fullname','roll_no']
    list_editable=['email', 'phone']
admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(Student,StudentAdmin)