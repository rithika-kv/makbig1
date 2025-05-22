from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
import random,string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import studentregistrationform,teacherloginform
from . models import dbstudent1,dbteacher1
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import dbstudent1
from django.http import HttpResponse
from .models import dbteacher1
from .forms import teacherloginform
from django.contrib import messages









def home(request):
    return render(request,"home.html")

def addteachers(request):
    emails = [
        "teacher10@gmail.com",
        "teacher2@gmail.com",
        "teacher3@gmail.com",
        "teacher4@gmail.com",
        "teacher5@gmail.com",
    ]
    passwords = [
        "102345",
        "23451",
        "34512",
        "45123",
        "51234",
    ]
    for email, password in zip(emails, passwords):
        dbteacher1.objects.create(t_email=email, t_password=password)
    return HttpResponse(" teachers added successfully")
def teacherlogin(request):
    form = teacherloginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['t_email']
            password = form.cleaned_data['t_password']

            try:
                teacher = dbteacher1.objects.get(t_email=email, t_password=password)
                request.session['teacher_email'] = teacher.t_email
                return redirect('app1:teacherdashboard')
            except dbteacher1.DoesNotExist:
                messages.error(request, 'Invalid credentials.')
        else:
            messages.error(request, 'Please correct the form errors.')
    return render(request, "teacherlogin.html", {'form': form})

def teacherdashboard(request):
    teacher_email = request.session.get('teacher_email', 'Unknown')
    return render(request, "teacherdashboard.html", {'teacher_email': teacher_email})

def teacherlogout(request):
    request.session.flush()  
    return redirect('app1:teacherlogin')

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import studentregistrationform
from .models import dbstudent1

def student_register(request):
    if request.method == 'POST':
        form = studentregistrationform(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            send_mail(
                'New student registration',
                f'Student {student.s_firstname} {student.s_lastname} has registered. Please review their details.',
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return render(request, "registrationsuccess.html")
    else:
        form = studentregistrationform()
    return render(request, "register.html", {'form': form})


from django.shortcuts import redirect, render
from django.contrib import messages
from .models import dbstudent1
from django.contrib.auth.hashers import check_password



def studentlogin(request):
    if request.method == 'POST':
        email = request.POST.get('s_email', '').strip()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, "Both fields are required.")
            return render(request, "studentlogin.html")

        try:
            student = dbstudent1.objects.get(s_email=email)

            if student.s_status != 'approved':
                messages.error(request, "Your account has not been approved yet.")
                return render(request, "studentlogin.html")

            # ✅ Secure password check
            if check_password(password, student.s_password):
                request.session['student_email'] = student.s_email
                return redirect('app1:studentdashboard')
            else:
                messages.error(request, "Invalid email or password.")

        except dbstudent1.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, "studentlogin.html")




from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from .models import dbstudent1
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.contrib.auth.hashers import make_password


@require_POST
@transaction.atomic
def approve_student(request, student_id):
    student = get_object_or_404(dbstudent1, pk=student_id)

    if student.s_status == 'approved':
        messages.info(request, f"Student {student.s_email} is already approved.")
        return redirect('app1:custom_admin_dashboard')

    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    student.s_status = 'approved'
    student.s_password = make_password(password)  # 🔒 Secure password hash
    student.save()


    try:
        send_mail(
            'Your Account Has Been Approved',
            f'Your login credentials:\n\nEmail: {student.s_email}\nPassword: {password}',
            settings.DEFAULT_FROM_EMAIL,
            [student.s_email],
            fail_silently=False,
        )
        messages.success(request, f"Student {student.s_email} approved and credentials sent.")
    except Exception as e:
        messages.error(request, f"Email sending failed: {e}")
    return redirect('app1:custom_admin_dashboard')

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import dbstudent1

@staff_member_required
def custom_admin_dashboard(request):
    students = dbstudent1.objects.all()
    return render(request, 'customadmindashboard.html', {'students': students})
@login_required
def studentdashboard(request):
    email=request.session.get('s_email')
    return render(request,"studentdashboard.html",{'s_email':email})
def studentlogout(request):
    request.session.flush()  
    return redirect('app1:studentlogin')

def studentprofile(request):
    student_email = request.session.get('student_email')
    if not student_email:
        return redirect('app1:studentlogin')

    try:
        student = dbstudent1.objects.get(s_email=student_email)
    except dbstudent1.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('app1:studentlogin')
    return render(request, 'studentprofile.html', {'student': student})


























































