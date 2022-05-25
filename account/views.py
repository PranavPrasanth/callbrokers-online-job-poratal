
from django.http import HttpResponse
from django.shortcuts import redirect,render
from .forms import signupForm,AuthForm,CommonForm,signupForm,CompanyForm,JobseekerForm,customerForm,engineerForm,clubbrokerForm
from django.contrib.auth import login,authenticate,logout

def home(request):
    return render(request,'account/home.html')

def signup_Jobseeker(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = JobseekerForm()
         context['form2'] = signupForm()
         return render(request,'account/jobseeker_reg.html',context) 
    elif request.method == 'POST':
         form1=JobseekerForm(request.POST)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'jobseeker'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1 
             context['form2']   = form2
             return render(request,'account/jobseeker_reg.html',context)
def signup_Company(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = CompanyForm()
         context['form2'] = signupForm()
         return render(request,'account/company_reg.html',context) 
    elif request.method == 'POST':
         form1=CompanyForm(request.POST)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'company'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1 
             context['form2']   = form2
             return render(request,'account/company_reg.html',context)





def signup_customer(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = customerForm()
         context['form2'] = signupForm()
         return render(request,'account/customer_reg.html',context) 
    elif request.method == 'POST':
         form1=customerForm(request.POST, request.FILES)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'customer'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1 
             context['form2']   = form2
             return render(request,'account/customer_reg.html',context)
                       
def signup_engineer(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = engineerForm()
         context['form2'] = signupForm()
         return render(request,'account/engineer_reg.html',context) 
    elif request.method == 'POST':
         form1=engineerForm(request.POST, request.FILES)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'engineer'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1 
             context['form2']   = form2
             return render(request,'account/engineer_reg.html',context)

def signup_clubbroker(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = clubbrokerForm()
         context['form2'] = signupForm()
         return render(request,'account/clubbroker_reg.html',context) 
    elif request.method == 'POST':
         form1=clubbrokerForm(request.POST)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'clubbroker'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1 
             context['form2']   = form2
             return render(request,'account/clubbroker_reg.html',context)


def login_view(request):
    if request.method =='GET':
        context = {}
        context['form'] = AuthForm()
        return render(request, 'account/signin.html', context)
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('/admin/')
            elif user.user_type =='customer':
                return redirect('customer_home')
            elif user.user_type =='jobseeker':
                return redirect('jobseeker_home')
            elif user.user_type =='company':
                return redirect('company_home')
            elif user.user_type =='engineer':
                return redirect('engineer_home')
            elif user.user_type =='clubbroker':
                return redirect('clubbroker_home')
        else:
            context = {}
            context['form'] = AuthForm()
            context['error'] = 'Invalid Credentials'
            return render(request, 'account/signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('account_login')

