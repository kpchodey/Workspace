from django.contrib import admin

# Register your models here.

from app.models import Appium, Storm, Revo, Set_Top_Box, Test_Suite

admin.site.register(Appium)
admin.site.register(Storm)
# admin.site.register(Revo)


class RevoAdmin(admin.ModelAdmin):
	list_display = ('SuiteName', 'Test_Case', 'FileName', 'Total_Action', 'Pass', 'Fail', 'Exe_Time', 'Result')
	list_filter = ['SuiteName', 'Test_Case', 'Total_Action', 'Pass', 'Fail', 'Exe_Time', 'Result']
	search_fields = ['SuiteName', 'Test_Case', 'Total_Action', 'Pass', 'Fail', 'Exe_Time', 'Result' ]


class Set_Top_BoxAdmin(admin.ModelAdmin):
	list_display = ('Device_Type', 'IP_Adress', 'Model_Name', 'Serial_Number')

class Test_Suite_Admin(admin.ModelAdmin):
	list_display = ['Test_Suite_Name']

admin.site.register(Revo, RevoAdmin)
admin.site.register(Test_Suite, Test_Suite_Admin)
admin.site.register(Set_Top_Box, Set_Top_BoxAdmin)
