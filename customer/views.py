from django.shortcuts import redirect, render
from account.forms import CommonForm, customerForm
from account.models import customer,engineer
from .forms import WorkForm, FeedbackForm
from .models import Work
from engineer.models import ApplyWork, Report

# Create your views here.
def customer_index(request):
    context = {}
    context['data'] = customer.objects.get(user=request.user)
    return render(request,'customer/customer.html',context) 

def profile(request):
    if request.method == 'GET':
         context = {}
         context['data'] = customer.objects.get(user=request.user)
         context['form1'] = customerForm(instance=context['data'])
         context['form2'] = CommonForm(instance=request.user)
         return render(request,'customer/profile.html',context) 
    elif request.method == 'POST':
        form1=customerForm(data=request.POST, files=request.FILES, instance=customer.objects.get(user=request.user))
        form2= CommonForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('customer_home')
        else:
            context = {}
            context['form1'] = form1 
            context['form2']   = form2
            return render(request,'customer/profile.html',context)

def change_password(request):
    data = customer.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        return render(request,'customer/change_password.html',context)
    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('customer_home')
            else:
                return render(request,'customer/change_password.html',{'error':'Old Password is wrong', 'data':data})
        else:
            return render(request,'customer/change_password.html',{'error':'New Password and Confirm Password is not same', 'data':data})

def create_work(request):
    data = customer.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        context['form'] = WorkForm()
        return render(request,'customer/create_work.html',context)
    elif request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('customer_create_work')
        else:
            context = {}
            context['data'] = data
            context['form'] = form
            return render(request,'customer/create_work.html',context)


def search_engineers(request):
    district = engineer.objects.all().values_list('district', flat=True).distinct()
    if request.method == 'GET':
        context = {}
        context['data'] = district
        return render(request,'customer/search_engineers.html',context)
    elif request.method == 'POST':
        context = {}
        dist = request.POST['dist']
        context['data'] = district
        context['engineers'] = engineer.objects.filter(district=dist)
        return render(request,'customer/search_engineers.html',context)


def manage_work(request):
    if request.method == 'GET':
        context = {}
        context['works'] = Work.objects.filter(user=request.user)
        return render(request,'customer/work_list.html',context)


def edit_work(request,work_id):
    work = Work.objects.get(id=work_id)
    if request.method == 'GET':
        context = {}
        context['form'] = WorkForm(instance=work)
        return render(request,'customer/edit_work.html',context)
    elif request.method == 'POST':
        form = WorkForm(data=request.POST, instance=work)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('customer_manage_work')
        else:
            context = {}
            context['form'] = form
            return render(request,'customer/edit_work.html',context)

def delete_work(request,work_id):
    work = Work.objects.get(id=work_id)
    work.delete()
    return redirect('customer_manage_work')


def work_request(request):
    works = ApplyWork.objects.filter(work=Work.objects.get(user=request.user))
    if request.method == 'GET':
        context = {}
        context['works'] = works
        return render(request,'customer/work_request.html',context)

def approve_work(request,app_work_id):
    work = ApplyWork.objects.get(id=app_work_id)
    work.status = 'Approved'
    work.save()
    return redirect('customer_work_request')

def reject_work(request,app_work_id):
    work = ApplyWork.objects.get(id=app_work_id)
    work.status = 'Rejected'
    work.save()
    return redirect('customer_work_request')

def feedback(request):
    if request.method == 'GET':
        context = {}
        context['form'] = FeedbackForm()
        return render(request,'customer/feedback.html',context)
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('customer_home')
        else:
            context = {}
            context['form'] = form
            return render(request,'customer/feedback.html',context)

def track_work(request):
    if request.method == 'GET':
        lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
        works = ApplyWork.objects.filter(work__in=lst,status__in=['Approved', 'Completed'])
        context = {}
        context['works'] = works
        return render(request,'customer/track_work.html',context)
    elif request.method == 'POST':
        filter_by = request.POST['filter']
        print(filter_by)
        if filter_by == 'all':
            return redirect('customer_track_work')
        if filter_by == 'in-progress':
            lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
            works = ApplyWork.objects.filter(work__in=lst,status='Approved')
            context = {}
            context['works'] = works
            return render(request,'customer/track_work.html',context)
        if filter_by == 'completed':
            lst = list(Work.objects.filter(user=request.user).values_list('id').distinct())
            works = ApplyWork.objects.filter(work__in=lst,status='Completed')
            context = {}
            context['works'] = works
            return render(request,'customer/track_work.html',context)

def open_report(request, work_id):
    if request.method == 'GET':
        context = {}
        context['reports'] = Report.objects.filter(work__work__id=work_id)
        return render(request,'customer/open_report.html',context)

# Create your views here.


