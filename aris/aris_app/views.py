from django.shortcuts import render
from django.views import View

# Create your views here.
class Dashboard(View):
    def get(self, request):

        template_name = 'admin/dashboard.html'
        return render(request, template_name)
