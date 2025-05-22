from django.urls import path
from.import views
app_name="app1"
urlpatterns=[
    # path('register_student',views.register_student,name="register_student"),
    # path('generate_password',views.generate_password,name="generate_password"),
    # path('studentlogin',views.studentlogin,name="studentlogin"),
    # path('studentdashboard',views.studentdashboard,name="studentdashboard")



    path('student_register',views.student_register,name="student_register"),
    path('approve_student',views.approve_student,name="approve_student"),
    path('approve-student/<int:student_id>/', views.approve_student, name='approve_student'),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('studentdashboard',views.studentdashboard,name="studentdashboard"),
    path('custom_admin_dashboard',views.custom_admin_dashboard,name="custom_admin_dashboard"),
    path('teacherlogin',views.teacherlogin,name="teacherlogin"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
    path('addteachers',views.addteachers,name="addteachers"),
    path('home',views.home,name="home"),
    path('studentlogout',views.studentlogout,name="studentlogout"),
    path('teacherlogout',views.teacherlogout,name="teacherlogout"),
    path('studentprofile',views.studentprofile,name="studentprofile")




]