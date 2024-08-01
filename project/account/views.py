from django.shortcuts import render
from account.tasks import sendEmail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def register(request) :
    data = request.data
    newuser = User.objects.create(
        username = data['username'],
        email = data['email'],
        password = data['password'],
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    msg = sendEmail.delay_on_commit(newuser.email, 'welcome to your account ')
    print(msg)
    
    return  Response({'details' : 'ok'})

