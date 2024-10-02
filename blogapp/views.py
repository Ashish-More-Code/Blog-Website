from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Count
from blogapp.models import Blogpost,Like

# Create your views here.
def home(request):
    u = Blogpost.objects.all()
    context = {}
    context['data'] = u
    trending_posts = Blogpost.objects.all().order_by('-likecount')
    print(trending_posts.query)  # Print the SQL query for debugging
    context['trending'] = trending_posts    
    return render(request,'index.html',context)

def bdetailshome(request,bid):
    myblog=Blogpost.objects.filter(id=bid)
    context={}
    context['data']=myblog
    return render(request,'bdetailfromhome.html',context)

def fetchCategory(request,cat):
    myblog=Blogpost.objects.filter(type=cat)
    context={}
    context['cat']=myblog
    return render(request,'index.html',context)


def like(request,bid):
    if request.user.is_authenticated:
        uid=request.user.id 
        u=User.objects.filter(id=uid)
        bpost=Blogpost.objects.filter(id=bid)

        if bpost and u:
            like = Like.objects.filter(blogpost=bpost[0], user=u[0]).first()
            if like:
                like.delete()
                bpost[0].likecount -= 1
                bpost[0].save()
            else:
                Like.objects.create(blogpost=bpost[0], user=u[0])
                bpost[0].likecount += 1
                bpost[0].save()

        context={}
        context['data']=bpost
        return render(request,'bdetailfromhome.html',context)
    else:
        return render(request,'login.html')


def registration(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        upass=request.POST['pass']
        ucpass=request.POST['cpass'] 
        if uname=="" or email=="" or upass=="" or ucpass=="":
            context={}
            context['errmsg']="Username and Password can not be empty"
            return render(request,'registration.html',context)
        elif upass != ucpass:
            context={}
            context['errmsg']="Password and confirm password does not match"
            return render(request,'registration.html',context)
        else:
            try:
                u=User.objects.create(username=uname,password=upass,email=email)
                u.set_password(upass)
                u.save()
                context={}
                context['successmsg']="Registration successful"
                return render(request,'registration.html',context)
            except Exception:
                context={}
                context['errmsg']="User with this username already exists!"
                return render(request,'registration.html',context)
    else:
        return render(request,'registration.html')

def ulogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        user = authenticate(username=uname, password=upass)
        if uname=="" or upass=="":
            context={}
            context['errmsg']="First enter the username and password"
            return render(request,'login.html',context)
        elif user is not None:
            context={}
            context['successmsg']="Login successful"
            login(request,user)
            return redirect('/')
        else:
            context={}
            context['errmsg']="Invalid username and password!"
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
    
def ulogout(request):
    logout(request)
    return redirect('/')

def createblog(request):
    uid=request.user.id
    u=User.objects.filter(id=uid)
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = datetime.now()
        type=request.POST.get('category')
        pimage = request.FILES.get('pimage')

        if title=="" or content=="" or content=="" or date=="" or pimage=="":
            context={}
            context["errmsg"]="All fields are mandatory !"
            return render(request,'createblog.html',context)
        else:
            context={}
            u=Blogpost.objects.create(userid=u[0],title=title,content=content,createdate=date,pimage=pimage,type=type)
            u.save()
            context['successmsg']='Great job! Your blog post is now live.'
            return render(request,'createblog.html',context)
    else:
        return render(request,'createblog.html')
    
def myblogs(request):
    uid=request.user.id
    u=User.objects.filter(id=uid)
    myblog=Blogpost.objects.filter(userid=u[0])
    context={}
    context["data"]=myblog
    return render(request,'myblogs.html',context)

def deletepost(request,bid):
    myblog=Blogpost.objects.filter(id=bid)
    print(myblog)
    myblog.delete()
    context={}
    context['data']=myblog
    return redirect('/myblogs')
    

def detailedblog(request,bid):
    myblog=Blogpost.objects.filter(id=bid)
    context={}
    context['data']=myblog
    return render(request,'detailedblog.html',context)
    
def editblog(request,bid):
    if request.method=="GET":
        myblog=Blogpost.objects.filter(id=bid)
        context={}
        context['data']=myblog
        return render(request,'editblog.html',context)
    else:
        title=request.POST['title']
        content=request.POST['content']
        if title=="" or content=="":
            myblog=Blogpost.objects.filter(id=bid)
            context={}
            context['data']=myblog
            context["errmsg"]="All fields are mandatory and cannot be empty !"
            return render(request,'editblog.html',context)
        else:
            Blogpost.objects.filter(id=bid).update(title=title, content=content)
            myblog=Blogpost.objects.filter(id=bid)
            context={}
            context['data']=myblog
            context['successmsg']="Blog Post Edited"
            return render(request,'editblog.html',context)


