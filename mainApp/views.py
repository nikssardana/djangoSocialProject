from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profileView(request):
    dictV = {}
    dictV['username'] = request.user.first_name
    if not request.user.first_name:
        dictV['username'] = request.user.username
    return render_to_response('profile.html',dictV)
