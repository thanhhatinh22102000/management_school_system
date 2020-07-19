import django_filters
from .models import Staff,Student,NotificationStaff,NotificationStudent,FeedBackStudent,FeedBackStaff

class studentfilters(django_filters.FilterSet):
    class Meta:
        model=Student
        fields=('name',)

class stafffilters(django_filters.FilterSet):
    class Meta:
        model=Staff
        fields=('name',)

class studentnotification(django_filters.FilterSet):
    class Meta:
        model=NotificationStudent
        fields='__all__'

class staffnotification(django_filters.FilterSet):
    class Meta:
        model=NotificationStaff
        fields='__all__'

class studentfeedback(django_filters.FilterSet):
    class Meta:
        model=FeedBackStudent
        fields='__all__'

class stafffeedback(django_filters.FilterSet):
    class Meta:
        model=FeedBackStaff
        fields='__all__'