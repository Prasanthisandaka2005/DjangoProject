from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm 
from django.contrib.auth.models import User
from django.contrib import auth 
from services.models import Service
from news.models import News,Image
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives
from news.forms import ImageForm

def Project(request):
    return HttpResponse("<b>Hello World</b>")

def courseDetails(request,courseid):
    return HttpResponse(courseid)



def Course(request):
    return HttpResponse("Welcome to<b> FirstProject</b>")

def submitform(request) :
    final_ans=0
    data = {}
    try:
        if request.method == 'POST':
        # N1=int(request.GET['num1'])
        # N2=int(request.GET['num2'])
            N1=int(request.POST.get('num1'))
            N2=int(request.POST.get('num2'))
            final_ans=(N1+N2)
            data = {
                'n1':N1,
                'n2':N2,
                'output':final_ans,
            }
            
            return HttpResponse(final_ans)
            
    except:
        pass


def homePage(request):


    # send_mail(
    #     'Testing Mail',
    #     'Here is the message',
    #     'prasanthisandaka05@gmail.com',
    #     ['prasanthisandaka2005@gmail.com'],
    #     fail_silently=False,

    # )
    newsData = News.objects.all()
    servicesData = Service.objects.all()
    paginator = Paginator(servicesData,4)
    page_number = request.GET.get('page')
    servicesDatafinal = paginator.get_page(page_number)
    totalPage=servicesDatafinal.paginator.num_pages


    # if request.method == "GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
    #         servicesData = Service.objects.filter(service_title__icontains=st)
            
    # for a in servicesData:
    #     print(a.service_icon)
    # print(Service)
    data = {
        'serviceData':servicesDatafinal,
        'lastpage':totalPage,
        'newsData':newsData,
        'totalPagelist':[n+1 for n in range(totalPage)]
    }

    
    return render(request,"index.html",data)

def newDetails(request,slug):
        newsDetails = News.objects.get(news_slug=slug)
        data = {
            'newsDetails' :newsDetails
        }
        return render(request,"calculator.html",data)

def Imageuploader(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img=Image.objects.all()
    data = {
        'form':form,
        'img':img
    }
    return render(request,"image-uploader.html",data)



def userForm(request):
    final_ans=0
    fn = usersForm()

    data = {'form':fn}
    try:
        if request.method == 'POST':
        # N1=int(request.GET['num1'])
        # N2=int(request.GET['num2'])
            N1=int(request.POST.get('num1'))
            N2=int(request.POST.get('num2'))
            final_ans=(N1+N2)
            data = {
                
                'form':fn,
                'output':final_ans,
            }
            url = '/?result={}'.format(final_ans)
            return redirect(url)
            
    except:
        pass

    return render(request,"userform.html",data)

def evenodd(request):
    result =""
    if request.method == 'POST':
        if request.POST.get('num') == "":
            return render(request,"evenodd.html",{'error':True})

        n = eval(request.POST.get('num'))
        if n%2 == 0:
            result = "Even Number"
        else:
            result = "Odd Number"

    return render(request,"evenodd.html",{'result':result})


def calculator(request):
   
    output = ""
    data = {}
    try:
        if request.method=='POST':
            value1=eval(request.POST.get('value-1'))
            opr=request.POST.get('options')
            value2=eval(request.POST.get('value-2'))
            if opr == '+':
                output = value1+value2
            elif opr == "-":
                output = value1-value2
            elif opr == "*":
                output = value1*value2
            elif opr == "/":
                output = value1/value2
            data = {
                'value1':value1,
                'value2':value2,
                'output':output,
            }

    except:
        output = "Invallid Operation....."
    return render(request,"calculator.html",data)


def signupview(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user  = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username, password=password1)
            user.save()
            return redirect('login')
        else:
            return render(request,'signup.html',{'error':'PAsswords do not match'})
   
    return render(request,'signup.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"Invalid username or password"})
    return render(request,'login.html')
