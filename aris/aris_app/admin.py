from django.contrib import admin
from .models import Members, Profile, Category, Product, BloodType, BloodDonor, AboutUs

# Register your models here.
admin.site.register(Members)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BloodType)
admin.site.register(BloodDonor)
admin.site.register(AboutUs)
