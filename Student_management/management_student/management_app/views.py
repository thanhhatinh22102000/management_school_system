from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Staff,Student,Subject,NotificationStudent,FeedBackStaff,FeedBackStudent,NotificationStaff
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .filters import studentfilters,stafffilters,staffnotification,studentnotification,studentfeedback,stafffeedback
from django.urls import reverse_lazy
from .forms import Registerform,FeedbackStaffForm,FeedbackStudentForm,NotificationStaffForm,NotificationStudentForm
from django.http import HttpResponseRedirect


# Create your views here.
class TrangChu(View):
    def get(self,request):
        return render(request,'management_app/trangchu.html')
# phần login-------------------------------------------------
class LoginStudent(View):
    def get(self,request):
        return render(request,'management_app/login_student.html')

    def post(self,request):
        username=request.POST.get('taikhoan')
        password=request.POST.get('matkhau')
        my_user=authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse('<center><h1>Không tồn tại user này!</h1></center>')
        else:
            login(request,my_user)
            return render(request,'management_app/function_student.html')

class LoginStaff(View):
    def get(self,request):
        return render(request,'management_app/login_staff.html')

    def post(self,request):
        username=request.POST.get('taikhoan')
        password=request.POST.get('matkhau')
        my_user=authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse('<center><h1>Không tồn tại user này!</h1></center>')
        else:
            login(request,my_user)
            return render(request,'management_app/function_staff.html')

class LoginAdmin(View):
    def get(self,request):
        return render(request,'management_app/login_admin.html')

    def post(self,request):
        username=request.POST.get('taikhoan')
        password=request.POST.get('matkhau')
        my_user=authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse('<center><h1>Không tồn tại user này!</h1></center>')
        else:
            login(request,my_user)
            return render(request,'management_app/function_admin.html')

class FunctionAdmin(View):
    def get(self,request):
        return render(request,'management_app/function_admin.html')

# phần logout----------------------------------------------------------------

def Logout_View(request):
    logout(request)

# phần view profile------------------------------------------------------------

def ViewProfileStudent(request):
    query=Student.objects.all()
    student_filter=studentfilters(request.GET,queryset=query)
    context={
        'form' :student_filter.form,
        'student' :student_filter.qs,
    }

    return  render(request,'management_app/student_profile.html',context)


def ViewProfileStaff(request):
    query = Staff.objects.all()
    staff_filter = stafffilters(request.GET, queryset=query)
    context = {
        'form': staff_filter.form,
        'staff': staff_filter.qs,
    }

    return render(request, 'management_app/staff_profile.html', context)
# phần view notification--------------------------------------------------
def ViewNotificationStudent(request):
    query=NotificationStudent.objects.all()
    N_student=studentnotification(request.GET,queryset=query)
    context={
        'form':N_student.form,
        'n_student':N_student.qs,
    }
    return render(request,'management_app/student_notification.html',context)

def ViewNotificationStaff(request):
    query=NotificationStaff.objects.all()
    N_staff=staffnotification(request.GET,queryset=query)
    context={
        'form':N_staff.form,
        'n_staff':N_staff.qs,
    }
    return render(request,'management_app/staff_notification.html',context)

def ViewFeedbackStudent(request):
    query=FeedBackStudent.objects.all()
    F_student=studentfeedback(request.GET,queryset=query)
    context={
        'form':F_student.form,
        'f_student':F_student.qs,
    }
    return render(request,'management_app/student_feedback.html',context)

def ViewFeedbackStaff(request):
    query=FeedBackStaff.objects.all()
    F_staff=stafffeedback(request.GET,queryset=query)
    context={
        'form':F_staff.form,
        'f_staff':F_staff.qs,
    }
    return render(request,'management_app/staff_feedback.html',context)

# register acount----------------------------------------------------------------

def Register(request):
    form = Registerform()
    if request.method=='POST':
        form =Registerform(request.POST)
        if form.is_valid():
            form.Save()
            return HttpResponseRedirect('/')
    return render(request,'management_app/register.html',{'form':form})
# feedback---------------------------------------------------------------------
def FeedbackStudent_Form(request):
    if request.method=='POST':
        form = FeedbackStudentForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'management_app/thanks.html')
    else:
        form = FeedbackStudentForm()
    return render(request,'management_app/feedbackstudent.html',{'form':form})

def FeedbackStaff_Form(request):
    if request.method=='POST':
        form = FeedbackStaffForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'management_app/thanks2.html')
    else:
        form = FeedbackStaffForm()
    return render(request,'management_app/feedbackstaff.html',{'form':form})

# admin managament--------------------------------------------------
class Student_View(DetailView):
    model = Student

class Staff_View(DetailView):
    model = Staff


class Student_List(ListView):
    model = Student


class Staff_List(ListView):
    model = Staff

def List_Student(request):
    query=Student.objects.all()
    student_filter=studentfilters(request.GET,queryset=query)
    context={
        'form' :student_filter.form,
        'student' :student_filter.qs,
    }

    return  render(request,'management_app/student_list.html',context)

def List_Staff(request):
    query=Staff.objects.all()
    staff_filter=stafffilters(request.GET,queryset=query)
    context={
        'form' :staff_filter.form,
        'staff' :staff_filter.qs,
    }

    return  render(request,'management_app/staff_list.html',context)

class Create_Student(CreateView):
    model = Student
    fields = ['id','name','email','address','gender','password']
    success_url = reverse_lazy('student')

class Create_Staff(CreateView):
    model = Staff
    fields = ['id','name','email','address','password']
    success_url = reverse_lazy('staff')


class Update_Student(UpdateView):
    model = Student
    fields = ['id', 'name', 'email', 'address', 'gender', 'password']
    success_url = reverse_lazy('student')


class Update_Staff(UpdateView):
    model = Staff
    fields = ['id', 'name', 'email', 'address', 'password']
    success_url = reverse_lazy('staff')

class Delete_Student(DeleteView):
    model = Student
    success_url = reverse_lazy('student')


class Delete_Staff(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff')

def NotiStudent_form(request):
    if request.method=='POST':
        form=NotificationStudentForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'management_app/thanks_stu.html')
    else:
        form=NotificationStudentForm()
        return render(request, 'management_app/noti_student.html', {'form': form})


def NotiStaff_form(request):
    if request.method == 'POST':
        form = NotificationStaffForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'management_app/thanks_sta.html')
    else:
        form = NotificationStaffForm()
        return render(request, 'management_app/noti_staff.html', {'form': form})