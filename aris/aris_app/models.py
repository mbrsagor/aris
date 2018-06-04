from django.db import models
from django.contrib.auth.models import User


# Member type
class Members(models.Model):
    member = models.CharField(max_length = 30)
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.member



# User Profile
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(max_length=25)
    address = models.CharField(max_length = 30)
    contact_number = models.IntegerField()
    member_type = models.ForeignKey(Members, on_delete = models.CASCADE)
    profile_photo = models.ImageField(upload_to = "users")
    create_at = models.DateTimeField( auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.username



# project category
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    category_image = models.ImageField(upload_to = 'project_category', blank= True, null = True)
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name




# Products
class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'project', blank= True, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank= True, null = True)
    model = models.CharField(max_length = 20)
    description = models.TextField()
    create_at = models.DateTimeField( auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name




# Blood Type
class BloodType(models.Model):
    name = models.CharField(max_length = 15)

    def __str__(self):
        return self.name



# Blood donors
class BloodDonor(models.Model):
    dononer_name = models.CharField(max_length = 30)
    dononer_desctric = models.CharField(max_length = 20)
    dononer_uplozilla = models.CharField(max_length = 20)
    dononer_village = models.CharField(max_length = 20)
    dononer_address = models.TextField()
    dononer_age = models.IntegerField()
    donoer_contact = models.IntegerField()
    bolood_type = models.ForeignKey(BloodType, on_delete = models.CASCADE)
    create_at = models.DateTimeField( auto_now = True)


    def __str__(self):
        return self.dononer_name


# About page Section
class AboutUs(models.Model):
    section_title = models.CharField(max_length = 20)
    section_desc = models.CharField(max_length = 50)
    aboutCompanyTitle = models.CharField(max_length = 40)
    about_text = models.TextField()
    about_image1 = models.ImageField(upload_to = 'about-us')
    about_image2 = models.ImageField(upload_to = 'about-us')


    def __str__(self):
        return self.section_title



# Service page section
class Service(models.Model):
    service_title = models.CharField(max_length = 35)
    service_icon = models.CharField(max_length = 20)
    service_heading = models.CharField(max_length = 25)
    tab_first_id = models.CharField(max_length = 10, blank = True, null = True, unique = True)
    tab_second_id = models.CharField(max_length = 10, blank = True, null = True, unique = True)
    service_image = models.ImageField(upload_to = 'service')
    service_text = models.TextField()
    create_at = models.DateTimeField( auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.service_title


# Portfoio page section
class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length = 20)
    portfolio_class = models.CharField(max_length = 10)
    portfolio_data_filter = models.CharField(max_length = 10)
    portfolio_image = models.ImageField(upload_to = 'portfolio')
    portfolio_image2 = models.ImageField(upload_to = 'portfolio')
    create_at = models.DateTimeField( auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.portfolio_title


# TEAM page section
class Team(models.Model):
    name = models.CharField(max_length = 30)
    designation = models.CharField(max_length = 40)
    profile_pic = models.ImageField(upload_to = 'team')
    create_at = models.DateTimeField( auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
