from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegister, AddItem, BloodDonor_Form, AboutUs_Form, Service_Form
from .models import *
# Message Framework
from django.contrib import messages


# homepage
def homepage_views(request):

    # about us section
    aboutus_obj = AboutUs.objects.all()

    # service section
    service_sec_obj = Service.objects.all()

    # blood donoet forms
    forms = BloodDonor_Form()
    if request.method == 'POST':
        forms = BloodDonor_Form(request.POST or None)
        if forms.is_valid():
            forms.save()
            return redirect(homepage_views)
    context = {
        'forms' : forms,
        'aboutus_obj' : aboutus_obj,
        'service_sec_obj' : service_sec_obj,
    }
    template_name = 'front-end/index.html'
    return render(request, template_name, context)



# Dashboard views
def dashboard_views(request):

    product_count = Product.objects.count()
    context = {
        'product_count' : product_count
    }
    template_name = 'admin/dashboard.html'
    return render(request, template_name)



# User Login views
def singin_views(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username, password = password)

        if auth is not None:
            login(request ,auth)
            messages.add_message(request, messages.INFO, 'Login success')
            return redirect(dashboard_views)
        else:
            messages.add_message(request, messages.INFO, "Username and Password doesn't Match")

    template_name = 'admin/login.html'
    return render(request, template_name)



# User Register views
def singup_views(request):

    forms = UserRegister(request.POST or None)
    if forms.is_valid():
        instance = forms.save(commit = False)
        instance.save()
        return redirect(singin_views)

    context = {
        'forms' : forms
    }
    template_name = 'admin/register.html'
    return render(request, template_name, context)


# Singout views
def singout_view(request):
    logout(request)
    return redirect(singin_views)



# Total list of users
def total_users(request):
    profile_obj = Profile.objects.all()
    forms = UserRegister()
    context = {
        'forms': forms,
        'profile_obj' : profile_obj
    }
    template_name = 'admin/list_of_users.html'
    return render(request, template_name, context)



# Product/Item
def add_new_item(request):
    forms = AddItem()
    if request.method == 'POST':
        forms = AddItem(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Item Added Successfully")
            return redirect(add_new_item)
    context = {
        'forms' : forms
    }
    template_name = 'admin/add_project.html'
    return render(request, template_name, context)



# Show project admin
def showProject_views(request):

    showProduct_obj = Product.objects.all()
    context = {
        'show_item' : showProduct_obj
    }
    template_name = 'admin/products.html'
    return render(request, template_name, context)



# Update Item
def updateItem_views(request, id):
    update_item = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        forms = AddItem(request.POST, request.FILES, instance = update_item)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, "Item updated Successfully")
            return redirect(showProject_views)
    else:
        forms = AddItem(instance = update_item)
    context = {
        'forms' : forms,
        'update_item' : update_item
    }
    template_name = 'admin/add_project.html'
    return render(request, template_name, context)



# delete items
def itemDelete_views(request, id):

    delete_item = get_object_or_404(Product, id = id)
    delete_item.delete()
    return redirect(showProject_views)



# blood donor views
def bloodDonorList_views(request):

    blood_donor_obj = BloodDonor.objects.all()
    context = {
        'blood_donor_obj' : blood_donor_obj
    }
    template_name = 'admin/blood_donor.html'
    return render(request, template_name, context)



# blood donor remove views
def bloodDonorRemove(request, id):

    remove_donor = get_object_or_404(BloodDonor, id = id)
    remove_donor.delete()
    return redirect(bloodDonorList_views)



# About us page
def aboutus_views(request):

    form = AboutUs_Form()
    if request.method == 'POST':
        form = AboutUs_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "About page save Successfully")
        else:
            messages.add_message(request, messages.INFO, "About page save Failed")
    context = {
        'form' : form
    }
    template_name = 'admin/about.html'
    return render(request, template_name, context)



# Update or edit about us page
def updateAbout_views(request, id):

    updateAbout_obj = get_object_or_404(AboutUs, id = id)
    if request.method == 'POST':
        form = AboutUs_Form(request.POST, request.FILES, instance = updateAbout_obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "About page update Successfully")
            return redirect(aboutus_views)
    else:
        form = AboutUs_Form(instance = updateAbout_obj)
    context = {
        'form' : form,
        'updateAbout_obj' : updateAbout_obj
    }
    template_name = 'admin/about.html'
    return render(request, template_name, context)


# server page section
def serverSection_views(request):

    form = Service_Form()
    if request.method == 'POST':
        form = Service_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Service update Successfully")
            return redirect(serverSection_views)
        else:
            messages.add_message(request, messages.INFO, "Service update failed")
    context = {
        'form' : form
    }

    template_name = 'admin/service.html'
    return render(request, template_name, context)



# All Services
def allService_views(request):

    all_service_obj = Service.objects.all()
    context = {
        'all_service_obj' :all_service_obj
    }
    template_name = 'admin/allservice.html'
    return render(request, template_name, context)



# Delete Services
def deleteService_views(request, id):

    delete_service_obj = get_object_or_404(Service, id = id)
    delete_service_obj.delete()
    messages.add_message(request, messages.INFO, "Service Delete Successfully")
    return redirect(allService_views)
