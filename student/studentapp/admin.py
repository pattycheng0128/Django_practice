from django.contrib import admin
from studentapp.models import student

# Register your models here.
# admin.site.register(student)
class studentAdmin(admin.ModelAdmin):
  list_display=('id', 'cName', 'cSex', 'cBirthday', 
                'cEmail', 'cPhone', 'cAddr')
  search_fields=('cName',)
  list_filter=('cName', 'cSex')
  ordering=('id',)
  
  
admin.site.register(student, studentAdmin)

