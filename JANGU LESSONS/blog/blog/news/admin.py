from django.contrib import admin
from news.models import Post,Student,ContactUs,Category,UseProfile
admin.site.site_header='Bizning website | It-school'
admin.site.site_title='E-commercial website'
class StudentAdmin(admin.ModelAdmin):
    list_display=['fullname','roll_no','email','phone','is_registered']
    list_filter=['fullname','roll_no']
    search_fields=['fullname','roll_no']
    list_editable=['email', 'phone']
admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(Category)
admin.site.register(UseProfile)
admin.site.register(Student,StudentAdmin)