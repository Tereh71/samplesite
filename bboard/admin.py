from django.contrib import admin


# Register your models here.
from .models import Bb
#створення в адмін частині зрозумілого інтерфейсу
class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content','price','published', 'rubric')
    list_display_links =  ('title','content')
    search_fields =  ('title','content')

admin.site.register(Bb, BbAdmin)

from .models import Rubric
admin.site.register(Rubric)
