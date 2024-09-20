from django.urls import path
from . import views

app_name = 'cvs'

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),  # Keep this one
    
    path('resume/', views.resume_view, name='resume'),
    
    # User Registration
    path('accounts/register/', views.register, name='register'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Profile Management
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Education Management
    path('add-education/', views.add_education, name='add_education'),
    #path('education/add/', views.add_education, name='add_education'),
    path('education/edit/<int:education_id>/', views.edit_education, name='edit_education'),
    path('education/delete/<int:education_id>/', views.delete_education, name='delete_education'),
    
    # Work Experience URLs
    path('work-experience/add/', views.add_work_experience, name='add_work_experience'),
    path('work-experience/edit/<int:experience_id>/', views.edit_work_experience, name='edit_work_experience'),
    path('work-experience/delete/<int:experience_id>/', views.delete_work_experience, name='delete_work_experience'),

    # Skill URLs
    path('skill/add/', views.add_skill, name='add_skill'),
    path('skill/edit/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('skill/delete/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    
    
    # CV Preview and Download
    path('cv/preview/', views.preview_cv, name='preview_cv'),
    path('cv/download/', views.download_cv, name='download_cv'),
]
