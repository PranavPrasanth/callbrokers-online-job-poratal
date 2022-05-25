from django.shortcuts import redirect, render
from account.forms import CommonForm, engineerForm
from account.models import engineer
from customer.models import Work
from .models import ApplyWork
from .forms import ReportForm

def engineer_index(request):
    context = {}
    context['data'] = engineer.objects.get(user=request.user)
    return render(request,'engineer/engineer.html',context) 


def profile(request):
    if request.method == 'GET':
         context = {}
         context['data'] = engineer.objects.get(user=request.user)
         context['form1'] = engineerForm(instance=context['data'])
         context['form2'] = CommonForm(instance=request.user)
         return render(request,'engineer/profile.html',context) 
    elif request.method == 'POST':
        form1=engineerForm(data=request.POST, files=request.FILES, instance=engineer.objects.get(user=request.user))
        form2= CommonForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('engineer_home')
        else:
            context = {}
            context['form1'] = form1 
            context['form2']   = form2
            return render(request,'engineer/profile.html',context)


def change_password(request):
    data = engineer.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        return render(request,'engineer/change_password.html',context)
    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('engineer_home')
            else:
                return render(request,'engineer/change_password.html',{'error':'Old Password is wrong', 'data':data})
        else:
            return render(request,'engineer/change_password.html',{'error':'New Password and Confirm Password is not same', 'data':data})

def work_list(request):
    context = {}
    context['works'] = Work.objects.exclude(id__in=ApplyWork.objects.filter(engineer=engineer.objects.get(user=request.user)).values_list('work', flat=True))
    return render(request,'engineer/work_list.html',context)

def apply_work(request, work_id):
    work = Work.objects.get(id=work_id)
    eng = engineer.objects.get(user=request.user)
    obj = ApplyWork.objects.create(work=work, engineer=eng)
    return redirect('engineer_home')


def applied_work(request):
    context = {}
    context['works'] = ApplyWork.objects.filter(engineer=engineer.objects.get(user=request.user), status='Applied')
    return render(request,'engineer/applied_work.html',context)

def approved_work(request):
    context = {}
    context['works'] = ApplyWork.objects.filter(engineer=engineer.objects.get(user=request.user), status='Approved')
    return render(request,'engineer/approved_work.html',context)


def create_report(request):
    if request.method == 'GET':
        context = {
            'form': ReportForm()
        }
        return render(request, 'engineer/report_create.html', context)
    elif request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            try:
                work = ApplyWork.objects.get(work__id=request.POST['work'], status="Approved")
                obj.work = work
                obj.save()
                work.status = "Completed"
                work.save()
                return redirect('engineer_approved_work')
            except:
                msg = "Work not found"
                return render(request, 'engineer/report_create.html', {'form':form, 'msg':msg})
        else:
            return render(request, 'engineer/report_create.html', {'form':form})

# Create your views here.
