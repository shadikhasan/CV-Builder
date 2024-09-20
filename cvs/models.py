from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)  # URL or path for profile image
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    career_objective = models.TextField(blank=True)  # Add career objective
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Image field for file upload

    def __str__(self):
        return self.full_name


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4, blank=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)  # GPA field added

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_date = models.DateField()  # Job start date
    end_date = models.DateField(blank=True, null=True)  # End date can be null
    responsibilities = models.TextField()  # List of job responsibilities

    def __str__(self):
        return self.job_title


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=80)  # Proficiency in percentage, default 80%

    def __str__(self):
        return self.skill_name
