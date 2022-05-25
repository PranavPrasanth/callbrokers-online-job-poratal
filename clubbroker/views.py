from django.shortcuts import redirect, render
from account.forms import CommonForm, clubbrokerForm
from account.models import clubbroker
from account.models import engineer
from customer.models import Work


# Create your views here.
def clubbroker_index(request):
    context = {}
    context['data'] = clubbroker.objects.get(user=request.user)
    return render(request,'clubbroker/clubbroker.html',context) 

def profile(request):
    if request.method == 'GET':
         context = {}
         context['data'] = clubbroker.objects.get(user=request.user)
         context['form1'] = clubbrokerForm(instance=context['data'])
         context['form2'] = CommonForm(instance=request.user)
         return render(request,'clubbroker/profile.html',context) 
    elif request.method == 'POST':
        form1=clubbrokerForm(data=request.POST, files=request.FILES, instance=clubbroker.objects.get(user=request.user))
        form2= CommonForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('clubbroker_home')
        else:
            context = {}
            context['form1'] = form1 
            context['form2']   = form2
            return render(request,'clubbroker/profile.html',context)

def change_password(request):
    data = clubbroker.objects.get(user=request.user)
    if request.method == 'GET':
        context = {}
        context['data'] = data
        return render(request,'clubbroker/change_password.html',context)
    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('clubbroker_home')
            else:
                return render(request,'clubbroker/change_password.html',{'error':'Old Password is wrong', 'data':data})
        else:
            return render(request,'clubbroker/change_password.html',{'error':'New Password and Confirm Password is not same', 'data':data})


def search_engineers(request):
    district = engineer.objects.all().values_list('district', flat=True).distinct()
    if request.method == 'GET':
        context = {}
        context['data'] = district
        return render(request,'clubbroker/search_engineers.html',context)
    elif request.method == 'POST':
        context = {}
        dist = request.POST['dist']
        context['data'] = district
        context['engineers'] = engineer.objects.filter(district=dist)
        return render(request,'clubbroker/search_engineers.html',context)


def work_list(request):
    if request.method == 'GET':
        context = {}
        context['works'] = Work.objects.all()
        return render(request,'clubbroker/work_list.html',context)
