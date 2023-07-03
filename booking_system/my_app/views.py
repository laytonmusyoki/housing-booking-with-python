from django.shortcuts import render,redirect
from .forms import CreateUser,Checkoutinputs,Houses_adding
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Houses,Checkout
from django.contrib.auth.models import User
from .decorators import allowed_users,unauthenticated_user
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(request):
    return render(request,'home.html')


@unauthenticated_user
def register(request):
    form=CreateUser
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect('signin')
    context={
        "form":form
    }
    return render(request,'register.html',context)


@unauthenticated_user
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f" Now you are logged in as {request.user}")
            return redirect('home')
        else:
            messages.warning(request,'Wrong credentials')
            return redirect('signin')
    return render(request,'login.html')

@login_required(login_url='signin')
def house(request):
    houses=Houses.objects.all()
    context={
        "houses":houses
       
    }
    return render(request,'house.html',context)


@login_required(login_url='signin')
def book(request,pk):
    
    houses=Houses.objects.get(id=pk)
    context={
        "house":houses,
       
    }
    return render(request,'book.html',context)


@login_required(login_url='signin')
def checkout(request):
    if request.user.is_authenticated:
        users=Checkout.objects.filter(user=request.user)
        form=Checkoutinputs
        context={
            "form":form,
            "forms":users
        }
        if request.method=='POST':
            form=Checkoutinputs(request.POST)
            if form.is_valid():
                form.save()
                if request.user.is_authenticated:
                    email=request.user.email
                subj='Placed order'
                messo='Thank you for choosing our houses as your future home! We are thrilled to have received your order and would like to express our gratitude for placing your trust in us.Use this TILL NUMBER 8137146 to pay '
                send_mail(
                    subj,
                    messo,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                messages.info(request,'You have booked successfully')
            else:
                messages.warning(request,'Please place order using your username')

                
        return render(request,'checkout.html',context)


@login_required(login_url='signin')
@allowed_users(user_roles=['admin'])
def adminpage(request):
    houses=Houses.objects.count()
    orders=Checkout.objects.count()
    # different house data retrive
    bedsitters=Houses.objects.filter(name='bedsitter').count()
    two_bedroom=Houses.objects.filter(name='two bedroom').count()
    three_bedroom=Houses.objects.filter(name='three bedroom').count()
    four_bedroom=Houses.objects.filter(name='four bedroom').count() 
    # booked houses
    bedsitter=Checkout.objects.filter(description='bedsitter').count()
    two_bedrooms=Checkout.objects.filter(description='two bedroom').count()
    three_bedrooms=Checkout.objects.filter(description='three bedroom').count()
    four_bedrooms=Checkout.objects.filter(description='four bedroom').count()
    house_no=Houses.objects.all()
    context={
        "houses":houses,
        "orders":orders,
        "bedsitter":bedsitter,
        "two_bedrooms":two_bedrooms,
        "three_bedrooms":three_bedrooms,
        "four_bedrooms":four_bedrooms,
        "vacant_sitter":bedsitters-bedsitter,
        "vacant_two":two_bedroom-two_bedrooms,
        "vacant_three":three_bedroom-three_bedrooms,
        "vacant_four":four_bedroom-four_bedrooms,

        "total_sitter":bedsitters,
        "total_two":two_bedroom,
        "total_three":three_bedroom,
        "total_four":four_bedroom,
        "house_no":house_no
        
    }

    return render(request,'admin.html',context)

@login_required(login_url='signin')
@allowed_users(user_roles=['admin'])
def addpage(request):
    form=Houses_adding
    if request.method=='POST':
        form=Houses_adding(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'House added successfully')
            return redirect('adminpage')
    context={
        "forms":form,
    }
    return render(request,'add.html',context)


@login_required(login_url='signin')
@allowed_users(user_roles=['admin'])
def update(request,pk):
    house=Houses.objects.get(id=pk)
    form=Houses_adding(instance=house)
    if request.method=='POST':
        form=Houses_adding(request.POST,request.FILES,instance=house)
        if form.is_valid():
            form.save()
            messages.success(request,'House has been updated successfully')
            return redirect('adminpage')
    context={
        "forms":form
    }
    return render(request,'update.html',context)


@login_required(login_url='signin')
@allowed_users(user_roles=['admin'])
def deletepage(request,pk):
    house=Houses.objects.get(id=pk)
    if request.method=='POST':
        house.delete()
        messages.success(request,'House has been deleted successfully')
        return redirect('adminpage')
    context={
        "form":house
    }
    return render(request,'delete.html',context)


def Logout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('signin')