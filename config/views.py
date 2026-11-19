from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from applications.models import Application
from accounts.models import User, CandidateProfile
from django.db.models import Count, Q


def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html',{'error': 'Invalid username or password'})
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        if role not in ['JOB_SEEKER', 'RECRUITER']:
            return render(request, 'register.html', {'error': 'Invalid user role'})
        User.objects.create_user(username=username,email=email,password=password,role=role)
        return redirect('login') 
    return render(request, 'register.html')



@login_required(login_url='login')
def dashboard_page(request):
    user = request.user
    stats = {}
    if user.role == 'JOB_SEEKER':
        applications = Application.objects.filter(applicant=user)
        stats = {
            'total_applications': applications.count(),
            'under_review': applications.filter(status='UNDER_REVIEW').count(),
            'shortlisted': applications.filter(status='SHORTLISTED').count(),
            'selected': applications.filter(status='SELECTED').count(),
            'rejected': applications.filter(status='REJECTED').count(),
        }
    elif user.role == 'RECRUITER':
        jobs = Job.objects.filter(recruiter=user)
        applications = Application.objects.filter(job__recruiter=user)
        stats = {
            'total_jobs': jobs.count(),
            'active_jobs': jobs.filter(is_active=True).count(),
            'total_applications': applications.count(),
            'under_review' : applications.filter(status='UNDER_REVIEW').count(),
            'shortlisted': applications.filter(status='SHORTLISTED').count(),
            'selected': applications.filter(status='SELECTED').count(),
            'rejected': applications.filter(status='REJECTED').count(),
        }
    elif user.role == 'ADMIN':
        stats = {
            'total_users': User.objects.count(),
            'total_job_seekers': User.objects.filter(role='JOB_SEEKER').count(),
            'total_recruiters': User.objects.filter(role='RECRUITER').count(),
            'total_jobs': Job.objects.count(),
            'active_jobs': Job.objects.filter(is_active=True).count(),
            'inactive_jobs': Job.objects.filter(is_active=False).count(),
            'total_applications': Application.objects.count(),
            'under_review': Application.objects.filter(status='UNDER_REVIEW').count(),
            'shortlisted': Application.objects.filter(status='SHORTLISTED').count(),
            'selected_applications': Application.objects.filter(status='SELECTED').count(),
            'rejected': Application.objects.filter(status='REJECTED').count(),
        }
    return render(request, 'dashboard.html', {'user': user,'stats': stats})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('dashboard')


def jobs_page(request):
    jobs = Job.objects.filter(is_active=True)
    search = request.GET.get('search', '').strip()
    if search:
        jobs = jobs.filter(
            Q(title__icontains=search) |
            Q(company_name__icontains=search) |
            Q(location__icontains=search))
    return render(request, 'jobs.html', {'jobs': jobs,'search': search})


def job_detail_page(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    already_applied = False
    if request.user.is_authenticated and request.user.role == 'JOB_SEEKER':
        already_applied = Application.objects.filter(
            job=job,applicant=request.user).exists()
    return render(request, 'job_detail.html', {
        'job': job,'already_applied': already_applied})


@login_required(login_url='login')
def apply_job(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    if request.method != 'POST':
        return redirect('job_detail', id=id)
    if request.user.role != 'JOB_SEEKER':
        messages.error(request, 'Only Job Seekers can apply.')
        return redirect('job_detail', id=id)
    application, created = Application.objects.get_or_create(
        job=job,applicant=request.user,defaults={'cover_letter': request.POST.get('cover_letter', '')})
    if created:
        messages.success(request, 'Application submitted successfully!')
    else:
        messages.warning(request, 'You have already applied for this job.')
    return redirect('job_detail', id=id)



@login_required(login_url='login')
def my_applications_page(request):
    if request.user.role != 'JOB_SEEKER':
        return redirect('dashboard')
    applications = Application.objects.filter(
        applicant=request.user).select_related('job').order_by('-applied_at')
    return render(request, 'my_applications.html', {'applications': applications})


@login_required(login_url='login')
def candidate_profile_page(request):
    if request.user.role != 'JOB_SEEKER':
        return redirect('dashboard')
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.phone_number = request.POST.get('phone_number', '')
        profile.location = request.POST.get('location', '')
        profile.professional_title = request.POST.get('professional_title', '')
        profile.bio = request.POST.get('bio', '')
        profile.education = request.POST.get('education', '')
        profile.experience_years = request.POST.get('experience_years', 0)
        profile.linkedin_url = request.POST.get('linkedin_url', '')
        profile.portfolio_url = request.POST.get('portfolio_url', '')
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('candidate_profile')
    return render(request, 'candidate_profile.html', {'profile': profile})


@login_required(login_url='login')
def resume_management_page(request):
    if request.user.role != 'JOB_SEEKER':
        return redirect('dashboard')
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        uploaded_resume = request.FILES.get('resume')
        if not uploaded_resume:
            messages.error(request, 'Please select a resume.')
        else:
            allowed_extensions = ['pdf', 'doc', 'docx']
            extension = uploaded_resume.name.rsplit('.', 1)[-1].lower()
            if extension not in allowed_extensions:
                messages.error(request, 'Only PDF, DOC and DOCX files are allowed.')
            elif uploaded_resume.size > 5 * 1024 * 1024:
                messages.error(request, 'Resume size must not exceed 5 MB.')
            else:
                old_resume = profile.resume
                profile.resume = uploaded_resume
                profile.save()
                if old_resume:
                    old_resume.delete(save=False)
                messages.success(request, 'Resume uploaded successfully!')
    return render(request, 'resume_management.html', {'profile': profile})


@login_required(login_url='login')
def recruiter_jobs_page(request):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    jobs = Job.objects.filter(recruiter=request.user).order_by('-created_at')
    return render(request, 'recruiter_jobs.html', {'jobs': jobs})


@login_required(login_url='login')
def create_job_page(request):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    if request.method == 'POST':
        Job.objects.create(
            recruiter=request.user,
            title=request.POST.get('title'),
            company_name=request.POST.get('company_name'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            job_type=request.POST.get('job_type'),
            salary_min=request.POST.get('salary_min') or None,
            salary_max=request.POST.get('salary_max') or None,
            experience_required=request.POST.get('experience_required'),
            skills_required=request.POST.get('skills_required')
        )
        messages.success(request, 'Job posted successfully!')
        return redirect('recruiter_jobs')
    return render(request, 'create_job.html')


@login_required(login_url='login')
def edit_job_page(request, id):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    job = get_object_or_404(Job,id=id,recruiter=request.user)
    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.company_name = request.POST.get('company_name')
        job.description = request.POST.get('description')
        job.location = request.POST.get('location')
        job.job_type = request.POST.get('job_type')
        job.salary_min = request.POST.get('salary_min') or None
        job.salary_max = request.POST.get('salary_max') or None
        job.experience_required = request.POST.get('experience_required')
        job.skills_required = request.POST.get('skills_required')
        job.save()
        messages.success(request, 'Job updated successfully!')
        return redirect('recruiter_jobs')
    return render(request, 'edit_job.html', {'job': job})


@login_required(login_url='login')
def delete_job_page(request, id):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    if request.method == 'POST':
        job = get_object_or_404(Job,id=id,recruiter=request.user)
        job.delete()
        messages.success(request,'Job deleted successfully!')
    return redirect('recruiter_jobs')


@login_required(login_url='login')
def recruiter_applications_page(request):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    applications = Application.objects.filter(job__recruiter=request.user
    ).select_related('job', 'applicant').order_by('-applied_at')
    return render(request, 'recruiter_applications.html', {'applications': applications})


@login_required(login_url='login')
def update_application_status_page(request, id):
    if request.user.role != 'RECRUITER':
        return redirect('dashboard')
    application = get_object_or_404(Application,id=id,job__recruiter=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        allowed_statuses = ['UNDER_REVIEW','SHORTLISTED','REJECTED','SELECTED']
        if new_status in allowed_statuses:
            application.status = new_status
            application.save()
            messages.success(request,'Application status updated successfully!')
    return redirect('recruiter_applications')