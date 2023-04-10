from django import forms
from .models import Resume

GENDER_CHOICES = [('Male', "Male"),
                  ('Female', 'Female')]

JOB_CHOICES = [('Delhi', "Delhi"),
               ('Pune', 'Pune'),
               ('Ranchi', "Ranchi"),
               ('Mumbai', 'Mumbai'),
               ('Banglore', "Banglore"),
               ('Chennai', 'Chennai'),]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations',
                                         choices=JOB_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'email',
                  'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']

        labels = {'name': 'Full Name', 'dob': 'Date of Birth', 'gender': 'Gender', 'locality': 'Locality', 'city': 'City',
                  'pin': 'Pin Cde', 'state': 'State', 'mobile': 'Mobile',  'profile_image': 'Profile Image', 'my_file': 'Document'
                  }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}), 'locality': forms.TextInput(attrs={'class': 'form-control'}), 'city': forms.TextInput(
            attrs={'class': 'form-control'}), 'pin': forms.NumberInput(attrs={'class': 'form-control'}), 'state': forms.Select(attrs={'class': 'form-control'}), 'mobile': forms.NumberInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}), }
