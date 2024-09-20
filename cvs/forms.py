# cvs/forms.py

from django import forms
from .models import Profile, Education, WorkExperience, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'contact_email', 'phone_number', 'address']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'responsibilities']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']
