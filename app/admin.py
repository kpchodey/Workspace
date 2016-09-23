from django.contrib import admin

# Register your models here.

from app.models import Appium, Storm, Revo, Set_Top_Box

admin.site.register(Appium)
admin.site.register(Storm)
# admin.site.register(Revo)


class RevoAdmin(admin.ModelAdmin):
	list_display = ('id_test_result', 'date', 'suite_name', 'project_name', 'test_case_id', 'author', 'tester', 'box_type', 'box_unit_adress', 'box_ip', 'total_actions', 'toatl_conditions', 'pass_numbers', 'fail_numbers', 'result', 'execution_time', 'test_job_name', 'test_job_executionid')
	list_filter = ['date', 'suite_name', 'project_name', 'test_case_id', 'author', 'tester', 'box_type', 'box_ip', 'pass_numbers', 'fail_numbers', 'result', 'execution_time', 'test_job_name',]
	search_fields = ['id_test_result', 'date', 'suite_name', 'project_name', 'test_case_id', 'author', 'tester', 'box_type', 'box_unit_adress', 'box_ip', 'total_actions', 'toatl_conditions', 'pass_numbers', 'fail_numbers', 'result', 'execution_time', 'test_job_name', 'test_job_executionid' ]


class Set_Top_BoxAdmin(admin.ModelAdmin):
	list_display = ('Device_Type', 'IP_Adress', 'Model_Name', 'Serial_Number')

admin.site.register(Revo, RevoAdmin)
admin.site.register(Set_Top_Box, Set_Top_BoxAdmin)