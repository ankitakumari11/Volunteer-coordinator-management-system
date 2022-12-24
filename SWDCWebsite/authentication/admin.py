from django.contrib import admin
from . models import IsCoord, RequestFrom, vdata

# Register your models here.

admin.site.register(RequestFrom)


class coordinfo(admin.ModelAdmin):
    list_display = ('cname', 'email', 'gender', 'dept',
                    'academic_year', 'div', 'current_add', 'module', 'prn', 'roll', 'contact_num')


admin.site.register(IsCoord, coordinfo)


class studentinfo(admin.ModelAdmin):
    list_display = ('Name', 'submitted', 'verified', 'email', 'gender', 'activity', 'dept',
                    'academic_year', 'div', 'contact_num', 'module', 'prn', 'roll', 'current_add', 'Objective_of_the_Activity', 'Description_of_the_Activity', 'Benefits_to_Society', 'Benefits_to_Self', 'Learning_Experiences_challenges', 'Cordinator', 'url')


admin.site.register(vdata, studentinfo)
