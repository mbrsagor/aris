from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Message Framework
from django.contrib import messages
# Send Mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Login decorator
from django.contrib.auth.decorators import login_required


# homepage
def homepage_views(request):

    # about us section
    aboutus_obj = AboutUs.objects.all()

    # service section
    service_sec_obj = Service.objects.all()

    # Portfolio
    portfolio_obj = Portfolio.objects.all()

    # Team Member
    all_member_obj = Team.objects.all()

    # Testimonial
    testimonail_obj = Testimonial.objects.all()

    # Brand
    brand_obj = Brand.objects.all()

    # Blog Post
    blogPost_obj = Blog.objects.all()

    # Instragram footer
    instragram_obj = Instragram.objects.all()

    # Contact form
    if request.method == 'GET':
        form = Contact_Form()
    else:
        form = Contact_Form(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, "From: "+from_email+"\n Message: "+message, message, ['admin@sagor.me'])
            except BadHeaderError:
                return HttpResponse('Message Send Failed')
            return redirect(homepage_views)


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
        'portfolio_obj' : portfolio_obj,
        'all_member_obj' : all_member_obj,
        'testimonail_obj' : testimonail_obj,
        'brand_obj' : brand_obj,
        'blogPost_obj' : blogPost_obj,
        'instragram_obj' : instragram_obj,
        'form' : form
    }
    template_name = 'front-end/index.html'
    return render(request, template_name, context)



# Dashboard views
@login_required(login_url='singin_views')
def dashboard_views(request):

    # count of project
    product_count = Product.objects.count()
    # count of bload dononer
    count_of_dononer = BloodDonor.objects.count()
    # Bload dononer
    list_of_dononer = BloodDonor.objects.all()
    # latest products
    latest_project = Product.objects.all()
    # Total users count
    total_users = Profile.objects.count()

    # Todo List
    form = TodoList_Form()
    if request.method == 'POST':
        form = TodoList_Form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return redirect(dashboard_views)

    show_todoList = Todolist.objects.all()

    context = {
        'product_count' : product_count,
        'list_of_dononer' : list_of_dononer,
        'count_of_dononer' : count_of_dononer,
        'latest_project' : latest_project,
        'total_users' : total_users,
        'form' : form,
        'show_todoList' : show_todoList
    }
    template_name = 'admin/dashboard.html'
    return render(request, template_name, context)



# User Login views
def singin_views(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username, password = password)

        if auth is not None:
            login(request ,auth)
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
        # Register usename validation
        # try:
        #      User.objects.get(username=username)
        # except User.DoesNotExist:
        #      messages.add_message(request, messages.INFO, "Username already exists")
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



# User Profile
@login_required(login_url='singin_views')
def profile_views(request):

    profile_obj = get_object_or_404(Profile, username = request.user)
    context = {
        'profile_obj' : profile_obj
    }
    template_name = 'admin/profile.html'
    return render(request, template_name, context)



# Add/Update Profile
@login_required(login_url='singin_views')
def addProfile_views(request):

    form = UserProfile_Form()
    if request.method == 'POST':
        form = UserProfile_Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Profile Updated Successfully")
            return redirect(profile_views)
        else:
            messages.add_message(request, messages.INFO, "Profile Updated Failed")
    context = {
        'form' : form
    }
    template_name = 'admin/add-profile.html'
    return render(request, template_name, context)



# Total list of users
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
def showProject_views(request):

    showProduct_obj = Product.objects.all()
    context = {
        'show_item' : showProduct_obj
    }
    template_name = 'admin/products.html'
    return render(request, template_name, context)



# Update Item
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
def itemDelete_views(request, id):

    delete_item = get_object_or_404(Product, id = id)
    delete_item.delete()
    return redirect(showProject_views)



# blood donor views
@login_required(login_url='singin_views')
def bloodDonorList_views(request):

    blood_donor_obj = BloodDonor.objects.all()
    context = {
        'blood_donor_obj' : blood_donor_obj
    }
    template_name = 'admin/blood_donor.html'
    return render(request, template_name, context)



# blood donor remove views
@login_required(login_url='singin_views')
def bloodDonorRemove(request, id):

    remove_donor = get_object_or_404(BloodDonor, id = id)
    remove_donor.delete()
    return redirect(bloodDonorList_views)



# About us page
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
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
@login_required(login_url='singin_views')
def allService_views(request):

    all_service_obj = Service.objects.all()
    context = {
        'all_service_obj' :all_service_obj
    }
    template_name = 'admin/allservice.html'
    return render(request, template_name, context)



# Delete Services
@login_required(login_url='singin_views')
def deleteService_views(request, id):

    delete_service_obj = get_object_or_404(Service, id = id)
    delete_service_obj.delete()
    messages.add_message(request, messages.INFO, "Service Delete Successfully")
    return redirect(allService_views)



# Update services
@login_required(login_url='singin_views')
def updateService_views(request, id):

    update_service_obj = get_object_or_404(Service, id = id)
    if request.method == 'POST':
        form = Service_Form(request.POST or None, request.FILES, instance = update_service_obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Service update Successfully")
        else:
            messages.add_message(request, messages.INFO, "Service update failed")
    else:
        form = Service_Form(instance = update_service_obj)
    context = {
        'form' : form,
        'update_service_obj' : update_service_obj,
    }
    template_name = 'admin/service.html'
    return render(request, template_name, context)



# Portfolio views
@login_required(login_url='singin_views')
def portfolio_views(request):

    form = Portfolio_Form()
    if request.method == 'POST':
        form = Portfolio_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Porftolio added Successfully")
            return redirect(portfolio_views)
        else:
            messages.add_message(request, messages.INFO, "Porftolio added failed")
    context = {
        'form' : form
    }
    template_name = 'admin/add-portfolio.html'
    return render(request, template_name, context)




# All Portfolio List
@login_required(login_url='singin_views')
def allportfolio_views(request):

    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list' : portfolio_list
    }
    template_name = 'admin/allportfolio.html'
    return render(request, template_name, context)



# Update portfolio
@login_required(login_url='singin_views')
def updatePportoflio(request, id):

    update_portfolio = get_object_or_404(Portfolio, id = id)
    if request.method == 'POST':
        form = Portfolio_Form(request.POST or None, request.FILES,  instance = update_portfolio)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Porftolio updated Successfully")
            return redirect(allportfolio_views)
        else:
            messages.add_message(request, messages.INFO, "Porftolio updated failed")
    else:
        form = Portfolio_Form(instance = update_portfolio)
    context = {
        'form' : form
    }
    template_name = 'admin/add-portfolio.html'
    return render(request, template_name, context)


# Delete Portfolio
@login_required(login_url='singin_views')
def deletePortfolio(request, id):

    delete_portfolio = get_object_or_404(Portfolio, id = id)
    delete_portfolio.delete()
    messages.add_message(request, messages.INFO, "Porftolio Delted Successfully")
    return redirect(allportfolio_views)



# Team Member section
@login_required(login_url='singin_views')
def teamMember_views(request):

    form = TeamMember_Form()
    if request.method == 'POST':
        form = TeamMember_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Team member added Successfully")
            return redirect(teamMember_views)
        else:
            messages.add_message(request, messages.INFO, "Team memeber added failed")
    context = {
        'form' : form
    }
    template_name = 'admin/add-temmeber.html'
    return render(request, template_name, context)



# all Memeber list
@login_required(login_url='singin_views')
def listOfAllMemeber_views(request):

    all_member_obj = Team.objects.all()
    context = {
        'all_member_obj' : all_member_obj
    }
    template_name = 'admin/allmember.html'
    return render(request, template_name, context)



# update Team Member views
@login_required(login_url='singin_views')
def updateTeamMember(request, id):

    update_member = get_object_or_404(Team, id = id)
    if request.method == 'POST':
        form = TeamMember_Form(request.POST or None, request.FILES, instance = update_member)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Team member updated Successfully")
            return redirect(listOfAllMemeber_views)
        else:
            messages.add_message(request, messages.INFO, "Team member updated failed")
    else:
        form = TeamMember_Form(instance = update_member)
    context = {
        'form' : form,
        'update_member' : update_member
    }
    template_name = 'admin/add-temmeber.html'
    return render(request, template_name, context)


# Delete Member
@login_required(login_url='singin_views')
def deleteMember_views(request, id):

    deleteMember_obj = get_object_or_404(Team, id = id)
    deleteMember_obj.delete()
    messages.add_message(request, messages.INFO, "Member deleted successfully")
    return redirect(listOfAllMemeber_views)




# Testimonial page section
@login_required(login_url='singin_views')
def testimonial_views(request):

    form = Testimonial_Form()
    if request.method == 'POST':
        form = Testimonial_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Testimonial added successfully")
            return redirect(testimonial_views)
        else:
            messages.add_message(request, messages.INFO, "Testimonial added failed")
    context = {
        'form' : form,
    }
    template_name = 'admin/add-testimonial.html'
    return render(request, template_name, context)




# All testimonial
@login_required(login_url='singin_views')
def allTestimonial_views(request):

    all_testmonial_obj = Testimonial.objects.all()
    context = {
        'all_testmonial_obj' : all_testmonial_obj
    }
    template_name = 'admin/alltestimonial.html'
    return render(request, template_name, context)



# Delete testmonial
@login_required(login_url='singin_views')
def testmonialDelete_views(request, id):

    delete_testmonial = get_object_or_404(Testimonial, id=id)
    delete_testmonial.delete()
    messages.add_message(request, messages.INFO, "Testimonial deleted successfully")
    return redirect(allTestimonial_views)



# Update testmonial
@login_required(login_url='singin_views')
def updateTestmonial_views(request, id):

    update_testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        form = Testimonial_Form(request.POST or None, request.FILES, instance = update_testimonial)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Testimonial updated successfully")
            return redirect(allTestimonial_views)
        else:
            messages.add_message(request, messages.INFO, "Testimonial updated failed")
    else:
        form = Testimonial_Form(instance = update_testimonial)

    context = {
        'form' : form,
    }
    template_name = 'admin/add-testimonial.html'
    return render(request, template_name, context)



# Brand Section
@login_required(login_url='singin_views')
def brand_views(request):

    form = Brand_Form()
    if request.method == 'POST':
        form = Brand_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Brand added successfully")
            return redirect(brand_views)
        else:
            messages.add_message(request, messages.INFO, "Brand updated failed")
    else:
        form = Brand_Form()
    context = {
        'form' : form
    }
    template_name = 'admin/add-brand.html'
    return render(request, template_name, context)




# Add Blog Post Category views
@login_required(login_url='singin_views')
def PostCategory_views(request):

    form = BlogCategory_Form()
    if request.method == 'POST':
        form = BlogCategory_Form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Category added successfully")
            return redirect(PostCategory_views)
        else:
            messages.add_message(request, messages.INFO, "Brand added failed")
    context = {
        'form' : form,
    }
    template_name = 'admin/add-category.html'
    return render(request, template_name, context)




# List of Category
@login_required(login_url='singin_views')
def allCategory_views(request):

    blog_category = BlogCategory.objects.all()
    context ={
        'blog_category' : blog_category
    }
    template_name = 'admin/allcategory.html'
    return render(request, template_name, context)



# Update Category views
@login_required(login_url='singin_views')
def updateCategory_veiws(request, id):

    updateBlog_category = get_object_or_404(BlogCategory, id = id)
    if request.method == 'POST':
        form = BlogCategory_Form(request.POST or None, instance = updateBlog_category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Category updated successfully")
            return redirect(allCategory_views)
        else:
            messages.add_message(request, messages.INFO, "Category updated failed")
    else:
        form = BlogCategory_Form(instance = updateBlog_category)
    context = {
        'form' : form
    }
    template_name = 'admin/add-category.html'
    return render(request, template_name, context)




# Delete Cateogry
@login_required(login_url='singin_views')
def deleteCategory_veiws(request, id):

    deleteBlog_category = get_object_or_404(BlogCategory, id = id)
    deleteBlog_category.delete()
    messages.add_message(request, messages.INFO, "Category deleted successfully")
    return redirect(allCategory_views)



# Blog post views
@login_required(login_url='singin_views')
def blogPost_views(request):

    form = BlogPost_Form()
    if request.method == 'POST':
        form = BlogPost_Form(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "Post puhblish successfully")
            return redirect(blogPost_views)
        else:
            messages.add_message(request, messages.INFO, "Post puhblish failed")
    context = {
        'form' : form
    }
    template_name = 'admin/add-post.html'
    return render(request, template_name, context)



# Display blog post
@login_required(login_url='singin_views')
def allwPost_views(request):

    allBlog_post = Blog.objects.all()
    context = {
        'allBlog_post' : allBlog_post
    }
    template_name = 'admin/allpost.html'
    return render(request, template_name, context)



# update blog post
@login_required(login_url='singin_views')
def updatePost_views(request, id):

    update_post = get_object_or_404(Blog, id = id)
    if request.method == 'POST':
        form = BlogPost_Form(request.POST or None, request.FILES, instance = update_post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Post updated successfully")
            return redirect(allwPost_views)
        else:
            messages.add_message(request, messages.INFO, "Post updated failed")
    else:
        form = BlogPost_Form(instance = update_post)
    context = {
        'form' : form
    }
    template_name = 'admin/add-post.html'
    return render(request, template_name, context)



# Delete blog post
@login_required(login_url='singin_views')
def deletePost_views(request, id):

    delete_post = get_object_or_404(Blog, id = id)
    delete_post.delete()
    messages.add_message(request, messages.INFO, "Post deleted successfully")
    return redirect(allwPost_views)



#  Instragram footer
@login_required(login_url='singin_views')
def instragram_views(request):

    form = Instragram_Form()
    if request.method == 'POST':
        form = Instragram_Form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.add_message(request, messages.INFO, "photo addded successfully")
            return redirect(instragram_views)
        else:
            messages.add_message(request, messages.INFO, "photo addded failed")
    context =  {
        'form' : form
    }
    template_name = 'admin/add-instragram.html'
    return render(request, template_name, context)



# Update Instragram
@login_required(login_url='singin_views')
def updateInstragram(request, id):

    instagram_update = get_object_or_404(Instragram, id = id)
    if request.method == 'POST':
        form = Instragram_Form(request.POST or None, instance = instagram_update)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "photo updated successfully")
            return redirect(allInstragram_views)
        else:
            messages.add_message(request, messages.INFO, "photo updated failed")
    else:
        form = Instragram_Form(instance = instagram_update)
    context = {
        'form' : form,
    }
    template_name = 'admin/add-instragram.html'
    return render(request, template_name, context)



# delete Instragram
@login_required(login_url='singin_views')
def deleteInstragram_views(request, id):
    instagram_delete = get_object_or_404(Instragram, id = id)
    instagram_delete.delete()
    messages.add_message(request, messages.INFO, "photo deleted successfully")
    return redirect(instragram_views)



# All Instragram
@login_required(login_url='singin_views')
def allInstragram_views(request):

    all_instragaram = Instragram.objects.all()
    context = {
        'all_instragaram' : all_instragaram
    }
    template_name = 'admin/allinstragaram.html'
    return render(request, template_name, context)



# Delete todo list
@login_required(login_url='singin_views')
def deleteTodoList(request, id):
    delete_todo_obj = get_object_or_404(Todolist, id = id)
    delete_todo_obj.delete()
    return redirect(dashboard_views)
