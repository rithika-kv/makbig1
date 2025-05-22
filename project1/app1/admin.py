from django.contrib import admin
from .models import dbstudent1
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import random,string
from django.conf import settings
# Register your models here.
# admin.site.register(dbstudent1)
def approve_students(modeladmin,request,queryset):
    for student in queryset:
        if student.s_status!='approved':
            password=''.join(random.choices(string.ascii_letters+string.digits,k=8))
            student.s_password=password
            student.status='approved'
            student.save()
            send_mail('your registration is approved',f'Username:{student.s_email}\nPassword:{password}',
                      settings.DEFAULT_FROM_EMAIL,[student.s_email],fail_silently=False,
                      )
            approve_students.short_description="approve selected students"


@admin.register(dbstudent1)
class studentadmin(admin.ModelAdmin):
    list_display=['s_email','s_firstname','s_lastname','s_status']
    actions=[approve_students]

