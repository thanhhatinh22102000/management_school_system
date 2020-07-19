from django.contrib import admin
from .models import Staff,Student,Subject,FeedBackStaff,FeedBackStudent,LeaveStaff,LeaveStudent,NotificationStaff,NotificationStudent
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'feedback', 'feedback_reply',)
    search_fields = ('id', 'student_id',)

    class Meta:
        model = FeedBackStudent

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(FeedBackStudent,FeedbackAdmin)
admin.site.register(FeedBackStaff)
admin.site.register(LeaveStudent)
admin.site.register(LeaveStaff)
admin.site.register(NotificationStaff)
admin.site.register(NotificationStudent)