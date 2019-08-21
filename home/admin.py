from django.contrib import admin
from home.models import Member, Activity, Message


class MemberAdmin(admin.ModelAdmin):
	list_display = ('mem_full_name_en', 'mem_current_points', 'mem_weekly_added_points')
	list_editable = ('mem_weekly_added_points',)
	readonly_fields = ('mem_last_points', 'mem_current_order_in_names', 'mem_last_order_in_names', 'mem_full_name_en', 'mem_full_name_ar',)
	
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('activity_week_number', 'activity_image', 'day_one_ar', 'day_two_ar', 'day_three_ar', 'day_four_ar', 'day_five_ar')
	list_editable = ('activity_image', 'day_one_ar', 'day_two_ar', 'day_three_ar', 'day_four_ar', 'day_five_ar',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Message)
