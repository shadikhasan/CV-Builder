from django import forms
from .models import Profile, Education, WorkExperience, Skill

# cvs/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'image', 'full_name', 'contact_email', 'phone_number', 'address', 'career_objective']
        labels = {
            'full_name': 'Full Name',
            'contact_email': 'Email Address',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'career_objective': 'Career Objective',
            'image': 'Profile Picture',
        }
        widgets = {
            'career_objective': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput(),  # For file input type (image)
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year', 'gpa']
        widgets = {
            'degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your degree',
            }),
            'institution': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter institution name',
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '5',
                'placeholder': 'Enter GPA (0.00 - 5.00)',
            }),
            'start_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start Year (YYYY)',
                'min': '1900',
                'max': '2099',
                'maxlength': '4',
            }),
            'end_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'End Year (YYYY)',
                'min': '1900',
                'max': '2099',
                'maxlength': '4',
            }),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'responsibilities']
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your job title',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the company name',
            }),
            'start_date': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),  # HTML5 date input
            'end_date': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),  # HTML5 date input
            'responsibilities': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your responsibilities',
                'rows': 5,
            }),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'proficiency']
        widgets = {
            'skill_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter skill name',
            }),
            'proficiency': forms.NumberInput(attrs={
                'class': 'form-control-range',  # Bootstrap range input
                'min': '0',
                'max': '100',
                'step': '1',
                'placeholder': 'Proficiency (0-100%)',
            }),
        }
