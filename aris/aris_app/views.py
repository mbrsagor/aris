from django.shortcuts import render
from django.views import View



# Dashboard views
class Dashboard(View):
    def get(self, request):

        template_name = 'admin/dashboard.html'
        return render(request, template_name)




# User Login views
def singin_views(request):

    context = {}
    template_name = 'admin/login.html'
    return render(request, template_name, context)
