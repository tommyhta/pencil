from django.shortcuts import render, HttpResponse, redirect
from apps.mainapp.models import *
from django.contrib import messages
from django.core import serializers
from . import handle_upload
import bcrypt


# Create your views here.

def index(request):

    return render(request, "mainapp/index.html")

def registration(request):

    return render(request, "mainapp/registration.html")

def welcome(request):

    return render(request,"mainapp/home.html")

def breached(request):
    return HttpResponse("You do not have permission to perform this action.")

def staff(request):
    if 'userID' not in request.session:
        request.session.clear()
        return redirect("/")
    else:
        if request.session['user'] < 4:
            request.session.clear()
            return redirect("/breached")
        else:
            user = User.objects.get(id=request.session['userID'])
            if request.session['sID'] != hash(user.created_at):
                request.session.clear()
                return redirect('/breached')
            if request.session['user'] != user.user_level:
                request.session.clear()
                return redirect('/breached')
            else:
                context = {
                    "products" : Product.objects.all()
                }
                return render(request,"mainapp/staff.html", context)

def admin(request):
    if 'userID' not in request.session:
        request.session.clear()
        return redirect("/")
    else:
        if request.session['user'] < 7:
            request.session.clear()
            return redirect("/breached")
        else:
            user = User.objects.get(id=request.session['userID'])
            if request.session['sID'] != hash(user.created_at):
                request.session.clear()
                return redirect('/breached')
            if request.session['user'] != user.user_level:
                request.session.clear()
                return redirect('/breached')
            else:
                context = {
                    "user" : user,
                    "users" : User.objects.order_by('-user_level')
                }
                return render(request,"mainapp/admin.html", context)

def user(request,id):
    if 'userID' not in request.session:
        request.session.clear()
        return redirect("/")
    else:
        user = User.objects.get(id=request.session['userID'])
        if request.session['sID'] != hash(user.created_at):
            request.session.clear()
            return redirect('/breached')
        if request.session['user'] != user.user_level:
            request.session.clear()
            return redirect('/breached')
        else:
            user = User.objects.get(id=id)
            context = {
            "user" : User.objects.get(id=id),
            }
            return render (request, "mainapp/user.html", context)


# ----------------------------------------LOGIN AND REGISTRATION----------------------------------------
def register(request):
    if request.method == 'POST':
        error = User.objects.validator(request.POST)
        if len(error):
            for key,value in error.items():
                messages.error(request, value, extra_tags=key)
            return redirect("reg")
        else:
            pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                user_level = 1,
                password_hash = pwhash
            )
            user = User.objects.get(email=request.POST['email'])
            request.session['name'] = user.first_name
            request.session['user'] = user.user_level
            request.session['userID'] = user.id
            request.session['sID'] = hash(user.created_at)
            return redirect("home")
    else:
        request.session.clear()
        return redirect("/")

def login(request):
    if request.method == 'POST':
        error = User.objects.loginValidator(request.POST)
        if len(error):
            for key,value in error.items():
                messages.error(request, value, extra_tags=key)
            return redirect("reg")
        else:
            if len(User.objects.filter(email=request.POST['emaillogin']))==0:
                messages.error(request,"You cannot be logged in.", extra_tags="bad")
                request.session.clear()
                return redirect("reg")
            else:
                user = User.objects.get(email=request.POST['emaillogin'])    
                if bcrypt.checkpw(request.POST['key'].encode(), user.password_hash.encode()):
                    request.session['name'] = user.first_name
                    request.session['user'] = user.user_level
                    request.session['userID'] = user.id
                    request.session['sID'] = hash(user.created_at)
                    return redirect("home")    
                else: 
                    messages.error(request,"You cannot be logged in.", extra_tags="bad")
                    request.session.clear()
                    return redirect("reg")       
    else:
        request.session.clear()
        return redirect("/")
# ----------------------------------------END LOGIN AND REGISTRATION----------------------------------------
def logout(request):
    request.session.clear()
    return redirect("/")

# ----------------------------------------ADMIN FORM----------------------------------------
def changetype(request):
    if request.method == "POST":
        user = User.objects.get(id = request.POST['userID'])
        if user.id == request.session["userID"]:
            messages.error(request,"You maynot change your own User Type", extra_tags="cantdothat")
            return redirect("/admins")
        else:
            if request.session['user'] < user.user_level or request.session['user'] == user.user_level:
                messages.error(request,"You do not have permission to do that.", extra_tags="cantdothat")
                return redirect("/admins")
            else:
                user.user_level = request.POST['type']
                user.save()
                messages.success(request,"You have successfully changed the User's type.", extra_tags="done")
                return redirect("/admins")
    else:
        request.session.clear()
        return redirect("/breached")

def deleteuser(request):
    if request.method == "POST":
        user = User.objects.get(id = request.POST['userID'])
        if user.user_level == 9 or user.user_level == 7:
            messages.error(request,"You maynot delete another Admin user", extra_tags="cantdothat")
            return redirect ("/admins")
        else:
            user.delete()
            messages.success(request,"You have successfully deleted a User.", extra_tags="done")
            return redirect ("/admins")
    else:
        request.session.clear()
        return redirect("/breached")

def adminsearch(request):
    if request.method == "POST":
        userSearched = request.POST['searchadmin']
        fname = User.objects.filter(first_name__contains = userSearched)
        lname = User.objects.filter(last_name__contains = userSearched)
        email = User.objects.filter(email__contains = userSearched)
        if len(fname):
            users = fname
        elif len(lname):
            users = lname
        elif len (email):
            users = email
        else:
            users = None
        context = {
            "users" : users,
        }
        return render(request, "mainapp/allusers.html", context)
    else: 
        request.session.clear()
        return redirect("/breached")

# ----------------------------------------ADMIN FORM----------------------------------------
# ----------------------------------------STAFF----------------------------------------
def addproduct(request):
    if request.method == "POST":
        if 'image' in request.FILES:
            filename = request.POST['model']+".jpeg"
            Product.objects.create(
                model = request.POST['model'],
                description = request.POST['description'],
                unit_price = request.POST['price'],
                status = request.POST['status'],
                quantity = request.POST['quantity'],
                image = filename
            )
            handle_upload.handle(request.FILES['image'], filename)
            return redirect("/staff")
        else:
            Product.objects.create(
                model = request.POST['model'],
                description = request.POST['description'],
                unit_price = request.POST['price'],
                status = request.POST['status'],
                quantity = request.POST['quantity'],
                image = "defaultimg.jpeg"
            )
            return redirect("/staff")
    else:
        request.session.clear()
        return redirect("/breached")

def deleteproduct(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST['product'])
        product.delete()
        messages.success(request,"You have successfully deleted the product.", extra_tags="productupdate")
        return redirect("/staff")
    else:
        request.session.clear()
        return redirect("/breached")

def editproduct(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST['product'])
        product.model = request.POST['model']
        product.description = request.POST['description']
        product.unit_price = request.POST['price']
        product.status = request.POST['status']
        product.quantity = request.POST['quantity']
        product.save()
        messages.success(request,"You have successfully update the product.", extra_tags="productupdate")
        return redirect("/staff")
    else:
        request.session.clear()
        return redirect("/breached")
# ----------------------------------------



