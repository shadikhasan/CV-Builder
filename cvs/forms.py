from django import forms
from .models import Profile, Education, WorkExperience, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'contact_email', 'phone_number', 'address', 'career_objective', 'image_url']
        widgets = {
            'career_objective': forms.Textarea(attrs={'rows': 3}),
            'image_url': forms.TextInput(attrs={'type': 'url'}),  # Ensures input for the image is a valid URL
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year', 'gpa']
        widgets = {
            'gpa': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '5'}),  # GPA as a number input
            'start_year': forms.TextInput(attrs={'type': 'text', 'maxlength': '4'}),
            'end_year': forms.TextInput(attrs={'type': 'text', 'maxlength': '4'}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'responsibilities']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),  # HTML5 date input
            'end_date': forms.TextInput(attrs={'type': 'date'}),  # HTML5 date input
            'responsibilities': forms.Textarea(attrs={'rows': 5}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'proficiency']
        widgets = {
            'proficiency': forms.NumberInput(attrs={'min': '0', 'max': '100'}),  # Proficiency input between 0-100%
        }
