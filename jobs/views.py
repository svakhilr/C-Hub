from django.shortcuts import render,redirect
from django.contrib.auth import  login,logout
from .forms import WorkerRegistrationForm,WorkerProfileUpdateForm,JobProfileForm
from users.forms import UserLoginForm
from users.models import WorkerProfile,JobProfile

import sweetify

def worker_signup(request):
    if request.method == "POST":
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request,user)
            sweetify.success(request , "Account Registered")
            return redirect('worker-dashboard')

    form = WorkerRegistrationForm()
    context = {
        "form":form
    }
    return render(request,'job/signup.html',context)

def worker_signin(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user =form.authenticate_user()
            
            if user:    
                login(request,user)
                sweetify.success(request,'Authenticated')
                return redirect('worker-dashboard')
            else:
                sweetify.error(request,'Invalid Credentials')

    form = UserLoginForm()
    context = {
        'form':form
    }
    return render(request,'job/signin.html',context)


def worker_signout(request):
    logout(request)
    sweetify.success(request,"Logged Out")
    return redirect('worker-signup')


def worker_dashboard(request):
    worker = request.user.worker
    job_profile = worker.job_profile
    profile_form = WorkerProfileUpdateForm(instance=worker)

    context = {
        "worker":worker,
        "profile_form":profile_form
    }
    return render(request,'job/dashboard.html',context)

def update_worker_profile(request):
    
    if request.method == "POST":
    
        profile =  WorkerProfile.objects.filter(user=request.user).update(profile_name=request.POST['profile_name'],profile_pic=request.FILES['profile_pic'])
        print(request.POST)
        print(request.FILES)
        
            
        return redirect('worker-dashboard')
    
def job_profile(request):
    worker = request.user.worker
    job_profiles =  JobProfile.objects.filter(worker=worker)
    context = {
        "job_profiles":job_profiles
    }
    return render(request,'job/jobprofile.html',context)

def add_job_profile(request):
    if request.method == 'POST':
        worker = request.user.worker
        form = JobProfileForm(request.POST,request.FILES)
        if form.is_valid():
            job_proile_form = form.save(commit=False)
            job_proile_form.worker=worker
            job_proile_form.save()                
            sweetify.success(request,'Profile Added Successfully')
            return redirect('job-profile')
    form = JobProfileForm()
    context = {
        "form":form
    }
    return render(request,'job/addjob.html',context)

def edit_job_profile(request,profile_id):
    profile = JobProfile.objects.get(id=profile_id)
    if request.method == 'POST':
        form = JobProfileForm(request.POST,request.FILES,instance=profile)


def view_jobprofiles(request):
    profiles = JobProfile.objects.all()
    context = {
        "profiles":profiles
    }
    return render(request,'shop/service.html',context)


