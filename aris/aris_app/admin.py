from django.contrib import admin
from .models import Members, Profile, Category, Product

# Register your models here.
admin.site.register(Members)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
