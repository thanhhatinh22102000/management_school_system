from django.urls import path
from . import views
urlpatterns = [
    path('',views.TrangChu.as_view(),name='trang_chu'),
    # url student--------------------------------------
    path('L-student',views.LoginStudent.as_view(),name='login_student'),
    path('view_profile_student',views.ViewProfileStudent,name='view_profile_student'),
    path('feedbackstudent',views.FeedbackStudent_Form,name='feedbackstudent'),
    path('notificationstudent',views.ViewNotificationStudent,name='noti_student'),



    # url staff---------------------------------------
    path('L-staff',views.LoginStaff.as_view(),name='login_staff'),
    path('view_profile_staff',views.ViewProfileStaff,name='view_profile_staff'),
    path('feedbackstaff',views.FeedbackStaff_Form,name='feedbackstaff'),
    path('notificationstaff',views.ViewNotificationStaff, name='noti_staff'),




    # url admin--------------------------------------
    path('L-admin',views.LoginAdmin.as_view(),name='login_admin'),
    path('function_ad',views.FunctionAdmin.as_view(),name='function_admin'),

    path('feed_stu',views.ViewFeedbackStudent,name='feed_stu'),
    path('feed_sta',views.ViewFeedbackStaff,name='feed_sta'),

    path('noti_stu',views.NotiStudent_form,name='noti_stu'),
    path('noti_sta',views.NotiStaff_form,name='noti_sta'),

    path('student',views.List_Student,name='student'),
    path('staff',views.List_Staff,name='staff'),

    path('view_stu/<int:pk>',views.Student_View.as_view(),name='student_view'),
    path('view_sta/<int:pk>',views.Staff_View.as_view(),name='staff_view'),

    path('create_stu/',views.Create_Student.as_view(),name='create_student'),
    path('create_sta/',views.Create_Staff.as_view(),name='create_staff'),

    path('view_stu/<int:pk>', views.Student_View.as_view(), name='student_view'),
    path('view_sta/<int:pk>', views.Staff_View.as_view(), name='staff_view'),

    path('update_sta/<int:pk>', views.Update_Staff.as_view(), name='update_staff'),
    path('update_stu/<int:pk>',views.Update_Student.as_view(),name='update_student'),

    path('delete_stu/<int:pk>',views.Delete_Student.as_view(),name='delete_student'),
    path('delete_sta/<int:pk>',views.Delete_Staff.as_view(),name='delete_staff'),

    # url register---------------------------------------
    path('register/',views.Register,name='register'),
    # url logout--------------------------------------------
    path('',views.Logout_View,name='logout'),
]