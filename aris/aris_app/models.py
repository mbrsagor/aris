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
    image = models.ImageField(upload_to = 'project_category', blank= True, null = True)
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
    donoer_contact = models.IntegerField()
    bolood_type = models.ForeignKey(BloodType, on_delete = models.CASCADE)


    def __str__(self):
        return self.dononer_name
