from django.contrib import admin
from .models import Members, Profile, Category, Product, BloodType, BloodDonor, AboutUs, Service, Portfolio, Team

# Register your models here.
admin.site.register(Members)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BloodType)
admin.site.register(BloodDonor)
admin.site.register(AboutUs)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Team)
