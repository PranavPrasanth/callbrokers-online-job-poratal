from django.shortcuts import redirect, render
from account.forms import CommonForm, JobseekerForm
from account.models import Company, Jobseeker
from company.models import Vaccany
from .models import ApplayJob
from customer.forms import FeedbackForm

def jobseeker_index(request):
    context = {}
    context['data'] = Jobseeker.objects.get(user=request.user)
    return render(request,'jobseeker/jobseeker.html',context) 


def profile(request):
    if request.method == 'GET':
         context = {}
         context['data'] = Jobseeker.objects.get(user=request.user)
         context['form1'] = JobseekerForm(instance=context['data'])
         context['form2'] = CommonForm(instance=request.user)
         return render(request,'jobseeker/profile.html',context) 
    elif request.method == 'POST':
        form1=JobseekerForm(data=request.POST, files=request.FILES, instance=Jobseeker.objects.get(user=request.user))
        form2= CommonForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('jobseeker_home')
        else:
            context = {}
            context['form1'] = form1 
            context['form2']   = form2
            return render(request,'jobseeker/profile.html',context)


def change_password(request):
    data = Jobseeker.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        return render(request,'jobseeker/change_password.html',context)
    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('jobseeker_home')
            else:
                return render(request,'jobseeker/change_password.html',{'error':'Old Password is wrong', 'data':data})
        else:
            return render(request,'jobseeker/change_password.html',{'error':'New Password and Confirm Password is not same', 'data':data})


def company_list(request):
    context = {}
    context['companies'] = Company.objects.all()
    return render(request,'jobseeker/company_list.html',context)


def job_list(request, company_id):
    jobs = Vaccany.objects.filter(user=company_id)
    if request.method == 'GET':
        context = {}
        context['jobs'] = jobs
        return render(request,'jobseeker/career.html',context)
    elif request.method == 'POST':
        jobseeker = Jobseeker.objects.get(user=request.user)
        job = Vaccany.objects.get(id=request.POST['job_id'])
        if ApplayJob.objects.filter(jobseeker=jobseeker, job=job).exists():
            return render(request,'jobseeker/career.html',{'jobs':jobs, 'error':'You have already applied for this job'})
        else:
            ApplayJob.objects.create(jobseeker=jobseeker, job=job)
            return redirect('jobseeker_company_list')


def job_applied(request):
    jobseeker = Jobseeker.objects.get(user=request.user)
    jobs = ApplayJob.objects.filter(jobseeker=jobseeker)
    context = {}
    context['jobs'] = jobs
    return render(request,'jobseeker/applied_job.html',context)

def delete_applied_job(request, job_id):
    job = ApplayJob.objects.get(id=job_id)
    job.delete()
    return redirect('jobseeker_applay_job')

def feedback(request):
    if request.method == 'GET':
        context = {}
        context['form'] = FeedbackForm()
        return render(request,'jobseeker/feedback.html',context)
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('jobseeker_home')
        else:
            context = {}
            context['form'] = form
            return render(request,'jobseeker/feedback.html',context)

# Create your views here.


# Create your views here.
