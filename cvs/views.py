# cvs/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import (
    ProfileForm,
    EducationForm,
    WorkExperienceForm,
    SkillForm
)
from .models import (
    Profile,
    Education,
    WorkExperience,
    Skill
)

# Home Page
def home(request):
    return render(request, 'cvs/home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create a Profile for the user
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# Dashboard
@login_required
def dashboard(request):
    try:
        profile = get_object_or_404(Profile, user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile does not exist. Please create a profile first.')
        return redirect('edit_profile')  # Adjust the redirect to your edit/create profile view

    educations = Education.objects.filter(profile=profile)
    experiences = WorkExperience.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)

    context = {
        'profile': profile,
        'educations': educations,
        'experiences': experiences,
        'skills': skills
    }
    return render(request, 'cvs/dashboard.html', context)

# Profile Management
@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('cvs:dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'cvs/edit_profile.html', {'form': form})


# Education Management
@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.profile = request.user.profile
            education.save()
            messages.success(request, 'Education added successfully.')
            return redirect('cvs:dashboard')
    else:
        form = EducationForm()
    return render(request, 'cvs/add_education.html', {'form': form})

@login_required
def edit_education(request, education_id):
    education = get_object_or_404(Education, id=education_id, profile=request.user.profile)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully.')
            return redirect('cvs:dashboard')
    else:
        form = EducationForm(instance=education)
    return render(request, 'cvs/edit_education.html', {'form': form})

@login_required
def delete_education(request, education_id):
    education = get_object_or_404(Education, id=education_id, profile=request.user.profile)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education deleted successfully.')
        return redirect('cvs:dashboard')
    return render(request, 'cvs/delete_education.html', {'education': education})

# Similar views for WorkExperience and Skill management...
@login_required
def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.profile = request.user.profile
            work_experience.save()
            messages.success(request, 'Work experience added successfully.')
            return redirect('cvs:dashboard')
    else:
        form = WorkExperienceForm()
    return render(request, 'cvs/add_work_experience.html', {'form': form})

@login_required
def edit_work_experience(request, experience_id):
    work_experience = get_object_or_404(WorkExperience, id=experience_id, profile=request.user.profile)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work experience updated successfully.')
            return redirect('cvs:dashboard')
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'cvs/edit_work_experience.html', {'form': form})

@login_required
def delete_work_experience(request, experience_id):
    work_experience = get_object_or_404(WorkExperience, id=experience_id, profile=request.user.profile)
    if request.method == 'POST':
        work_experience.delete()
        messages.success(request, 'Work experience deleted successfully.')
        return redirect('cvs:dashboard')
    return render(request, 'cvs/delete_work_experience.html', {'work_experience': work_experience})

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = request.user.profile
            skill.save()
            messages.success(request, 'Skill added successfully.')
            return redirect('cvs:dashboard')
    else:
        form = SkillForm()
    return render(request, 'cvs/add_skill.html', {'form': form})

@login_required
def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, profile=request.user.profile)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('cvs:dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'cvs/edit_skill.html', {'form': form})

@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, profile=request.user.profile)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully.')
        return redirect('cvs:dashboard')
    return render(request, 'cvs/delete_skill.html', {'skill': skill})

# CV Preview
@login_required
def preview_cv(request):
    profile = get_object_or_404(Profile, user=request.user)
    educations = Education.objects.filter(profile=profile)
    experiences = WorkExperience.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'educations': educations,
        'experiences': experiences,
        'skills': skills
    }
    return render(request, 'cvs/preview_cv.html', context)



# @login_required
def resume_view(request):
    profile = Profile.objects.get(user=request.user)
    educations = Education.objects.filter(profile=profile)
    work_experiences = WorkExperience.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)

    context = {
        'profile': profile,
        'educations': educations,
        'work_experiences': work_experiences,
        'skills': skills
    }
    return render(request, 'cvs/resume.html', context)

# CV Download as PDF
@login_required
def download_cv(request):
    # Placeholder response for the backend PDF logic
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # This response is sent when triggered via AJAX
        return HttpResponse(status=200)  # Success response
    else:
        return HttpResponse("<h1>Coming soon..</h1>")

