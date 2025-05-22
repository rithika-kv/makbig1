from django import forms
from . models import dbstudent1

# class studentregistrationform(forms.ModelForm):
#     class Meta:
#         model = dbstudent1
#         fields = ['s_profilepicture', 's_firstname', 's_lastname', 's_email', 's_phonenumber', 's_guardianphonenumber', 's_qualification']
#         labels = {
#             's_profilepicture': 'PROFILE PICTURE',
#             's_firstname': 'FIRST NAME',
#             's_lastname': 'LAST NAME',
#             's_email': 'EMAIL',
#             's_phonenumber': 'PHONE NUMBER',
#             's_guardianphonenumber': 'GUARDIAN PHONE NUMBER',
#             's_qualification': 'QUALIFICATION',
#         }
#         widgets = {
#             's_firstname': forms.TextInput(attrs={'class': 'form-control'}),
#             's_lastname': forms.TextInput(attrs={'class': 'form-control'}),
#             's_email': forms.EmailInput(attrs={'class': 'form-control'}),
#             's_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
#             's_guardianphonenumber': forms.TextInput(attrs={'class': 'form-control'}),
#             's_qualification': forms.Select(attrs={'class': 'form-control'}),
#         }


class teacherloginform(forms.Form):  # This must match exactly
    t_email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    t_password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))










# from django import forms
# from .models import dbstudent1

# class studentregistrationform(forms.ModelForm):
#     password = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput,
#         min_length=8
#     )
#     confirm_password = forms.CharField(
#         label='Confirm Password',
#         widget=forms.PasswordInput
#     )

#     class Meta:
#         model = dbstudent1
#         fields = [
#             's_profilepicture',
#             's_firstname',
#             's_lastname',
#             's_email',
#             's_phonenumber',
#             's_guardianphonenumber',
#             's_qualification'
#         ]

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data








# class studentregistrationform(forms.ModelForm):
#     class Meta:
#         model = dbstudent1
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(studentregistrationform, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({
#                 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
#             })








# from django import forms
# from .models import dbstudent1

# class studentregistrationform(forms.ModelForm):
#     class Meta:
#         model = dbstudent1
#         fields = [
#             's_profilepicture',
#             's_firstname',
#             's_lastname',
#             's_email',
#             's_phonenumber',
#             's_guardianphonenumber',
#             's_qualification',
#         ]
#         labels = {
#             's_profilepicture': 'Profile Picture',
#             's_firstname': 'First Name',
#             's_lastname': 'Last Name',
#             's_email': 'Email',
#             's_phonenumber': 'Phone Number',
#             's_guardianphonenumber': 'Guardian Phone Number',
#             's_qualification': 'Qualification',
#         }

#     def __init__(self, *args, **kwargs):
#         super(studentregistrationform, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({
#                 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
#             })


























# from django import forms
# from .models import dbstudent1

# class studentegistrationform(forms.ModelForm):
#     # Define choices for qualification field
#     QUALIFICATION_CHOICES = [
#         ('higher-secondary', 'Higher Secondary (12th Grade)'),
#         ('diploma', 'Diploma'),
#         ('bachelors', 'Bachelor\'s Degree'),
#         ('masters', 'Master\'s Degree'),
#         ('phd', 'PhD'),
#         ('other', 'Other'),
#     ]
    
#     # Add this to render qualification as a select dropdown
#     s_qualification = forms.ChoiceField(
#         choices=QUALIFICATION_CHOICES,
#         widget=forms.Select(attrs={'class': 'w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500'})
#     )

#     class Meta:
#         model = dbstudent1
#         fields = ['s_profilepicture', 's_firstname', 's_lastname', 's_email', 's_phonenumber', 's_guardianphonenumber', 's_qualification']









































from django import forms
from .models import dbstudent1

class studentregistrationform(forms.ModelForm):
    QUALIFICATION_CHOICES = [
        ('Higher Secondary', 'Higher Secondary (12th Grade)'),
        ('Diploma', 'Diploma'),
        ('Bachelors', "Bachelor's Degree"),
        ('Masters', "Master's Degree"),
        ('PhD', 'PhD'),
        ('Other', 'Other'),
    ]

    s_qualification = forms.ChoiceField(choices=QUALIFICATION_CHOICES, widget=forms.Select(
        attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'}
    ))

    class Meta:
        model = dbstudent1
        fields = [
            's_profilepicture', 's_firstname', 's_lastname', 's_email',
            's_phonenumber', 's_guardianphonenumber', 's_qualification'
        ]
        widgets = {
            's_profilepic': forms.ClearableFileInput(attrs={'class': 'hidden', 'id': 'id_s_profilepic'}),
            's_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            's_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            's_email': forms.EmailInput(attrs={'class': 'form-control'}),
            's_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            's_guardianphonenumber': forms.TextInput(attrs={'class': 'form-control'}),
        }
