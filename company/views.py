from django.shortcuts import redirect, render
from account.forms import CommonForm, CompanyForm
from account.models import Company, engineer
from .models import Vaccany
from .forms import VaccanyForm
from customer.forms import  WorkForm
from customer.models import Work
from jobseeker.models import ApplayJob
from engineer.models import ApplyWork, Report

def company_index(request):
    context = {}
    context['data'] = Company.objects.get(user=request.user)
    return render(request,'company/company.html',context) 


def profile(request):
    if request.method == 'GET':
         context = {}
         context['data'] = Company.objects.get(user=request.user)
         context['form1'] = CompanyForm(instance=context['data'])
         context['form2'] = CommonForm(instance=request.user)
         return render(request,'company/profile.html',context) 
    elif request.method == 'POST':
        form1=CompanyForm(data=request.POST, files=request.FILES, instance=Company.objects.get(user=request.user))
        form2= CommonForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('company_home')
        else:
            context = {}
            context['form1'] = form1 
            context['form2']   = form2
            return render(request,'company/profile.html',context)


def change_password(request):
    data = Company.objects.get(user=request.user.id)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        return render(request,'company/change_password.html',context)
    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('company_home')
            else:
                return render(request,'company/change_password.html',{'error':'Old Password is wrong', 'data':data})
        else:
            return render(request,'company/change_password.html',{'error':'New Password and Confirm Password is not same', 'data':data})

def create_work(request):
    data = Company.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        context['form'] = WorkForm()
        return render(request,'company/create_work.html',context)
    elif request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('company_create_work')
        else:
            context = {}
            context['data'] = data
            context['form'] = form
            return render(request,'company/create_work.html',context)



def create_vaccancy(request):
    data = Company.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        context['form'] = VaccanyForm()
        return render(request,'company/create_vaccancy.html',context)
    elif request.method == 'POST':
        form = VaccanyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('company_create_vaccancy')
        else:
            context = {}
            context['data'] = data
            context['form'] = form
            return render(request,'company/create_vaccancy.html',context)

def search_engineers(request):
    district = engineer.objects.all().values_list('district', flat=True).distinct()
    if request.method == 'GET':
        context = {}
        context['data'] = district
        return render(request,'company/search_engineers.html',context)
    elif request.method == 'POST':
        context = {}
        dist = request.POST['dist']
        context['data'] = district
        context['engineers'] = engineer.objects.filter(district=dist)
        return render(request,'company/search_engineers.html',context)


def work_list(request):
    if request.method == 'GET':
        context = {}
        context['works'] = Work.objects.filter(user=request.user)
        return render(request,'company/work_list.html',context)


def edit_work(request,work_id):
    work = Work.objects.get(id=work_id)
    if request.method == 'GET':
        context = {}
        context['form'] = WorkForm(instance=work)
        return render(request,'company/edit_work.html',context)
    elif request.method == 'POST':
        form = WorkForm(data=request.POST, instance=work)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('company_manage_work')
        else:
            context = {}
            context['form'] = form
            return render(request,'company/edit_work.html',context)

def delete_work(request,work_id):
    work = Work.objects.get(id=work_id)
    work.delete()
    return redirect('company_manage_work')


def vaccancy_list(request):
    if request.method == 'GET':
        context = {}
        context['vaccancies'] = Vaccany.objects.filter(user=request.user)
        return render(request,'company/vaccancy_list.html',context)


def edit_vaccancy(request,v_id):
    work = Vaccany.objects.get(id=v_id)
    if request.method == 'GET':
        context = {}
        context['form'] = VaccanyForm(instance=work)
        return render(request,'company/edit_vaccancy.html',context)
    elif request.method == 'POST':
        form = VaccanyForm(data=request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('company_vaccancy_list')
        else:
            context = {}
            context['form'] = form
            return render(request,'company/edit_vaccancy.html',context)

def delete_vaccancy(request,v_id):
    obj = Vaccany.objects.get(id=v_id)
    obj.delete()
    return redirect('company_vaccancy_list')

def job_application_list(request):
    if request.method == 'GET':
        context = {}
        context['applications'] = ApplayJob.objects.filter(job__user=request.user)
        return render(request,'company/job_application_list.html',context)

def accept_application(request,app_id):
    obj = ApplayJob.objects.get(id=app_id)
    obj.status = 'Accepted'
    obj.save()
    return redirect('company_job_applications')

def reject_application(request,app_id):
    obj = ApplayJob.objects.get(id=app_id)
    obj.status = 'Rejected'
    obj.save()
    return redirect('company_job_applications')


def work_request(request):
    lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
    works = ApplyWork.objects.filter(work__in=lst,status='Applied')
    if request.method == 'GET':
        context = {}
        context['works'] = works
        return render(request,'company/work_request.html',context)

def approve_work(request,app_work_id):
    work = ApplyWork.objects.get(id=app_work_id)
    work.status = 'Approved'
    work.save()
    return redirect('company_work_request')

def reject_work(request,app_work_id):
    work = ApplyWork.objects.get(id=app_work_id)
    work.status = 'Rejected'
    work.save()
    return redirect('company_work_request')

def track_work(request):
    if request.method == 'GET':
        lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
        works = ApplyWork.objects.filter(work__in=lst,status__in=['Approved', 'Completed'])
        context = {}
        context['works'] = works
        return render(request,'company/track_work.html',context)
    elif request.method == 'POST':
        filter_by = request.POST['filter']
        print(filter_by)
        if filter_by == 'all':
            return redirect('company_track_work')
        if filter_by == 'in-progress':
            lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
            works = ApplyWork.objects.filter(work__in=lst,status='Approved')
            context = {}
            context['works'] = works
            return render(request,'company/track_work.html',context)
        if filter_by == 'completed':
            lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
            works = ApplyWork.objects.filter(work__in=lst,status='Completed')
            context = {}
            context['works'] = works
            return render(request,'company/track_work.html',context)

def open_report(request, work_id):
    if request.method == 'GET':
        context = {}
        context['reports'] = Report.objects.filter(work__work__id=work_id)
        return render(request,'company/open_report.html',context)
# Create your views here.

