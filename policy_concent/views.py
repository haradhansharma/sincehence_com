from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control

def set_concent(request):    
    request.session['concent_given'] = 'True'  
    referrer = request.META.get('HTTP_REFERER')  # Get the referring URL
    return HttpResponseRedirect(referrer)