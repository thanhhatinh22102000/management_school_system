from django import forms
from django.contrib.auth.models import User
from .models import FeedBackStudent,FeedBackStaff,NotificationStudent,NotificationStaff

class Registerform(forms.Form):
    username=forms.CharField(label='Tài khoản',max_length=30)
    email=forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật Khẩu', widget=forms.PasswordInput())
    password2=forms.CharField(label='Nhập lại mật khẩu',widget=forms.PasswordInput())

    def Clean_Password2(self):
        if'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError('Mật khẩu không hợp lệ!')

    def Clean_User(self):
        username=self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')

    def Save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'])

    # feedback----------------------------------------------------------------------

class FeedbackStudentForm(forms.ModelForm):
    class Meta:
        model=FeedBackStudent
        exclude=[]

class FeedbackStaffForm(forms.ModelForm):
    class Meta:
        model=FeedBackStaff
        exclude=[]

class NotificationStaffForm(forms.ModelForm):
    class Meta:
        model=NotificationStaff
        exclude=[]

class NotificationStudentForm(forms.ModelForm):
    class Meta:
        model=NotificationStudent
        exclude=[]