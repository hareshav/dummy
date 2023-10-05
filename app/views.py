from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import myModel,Student
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.models import User
from .serializers import mymodelserial
class myModel(generics.ListCreateAPIView):
    queryset=myModel.objects.all()
    serializer_class=mymodelserial
@api_view(['POST'])
def send_data_to_DataBase(request):
    if request.method=='POST':
        print(request.data)
        umail=request.data.get('email')
        pword=request.data.get('password')
        print(umail,pword)
        # username=User.objects.get(email=umail).username
        #error raised when wrong password is provided
        # usermodel=get_user_model()
        try:
            username=User.objects.get(email=umail.lower()).username
            user1=authenticate(request,username=username,password=pword)
            if user1 is not None:
                login(request,user1)
                return JsonResponse({"email":umail},status=200)
            else:
                return JsonResponse({"dummy":umail})
        except Exception as e:
            print(e)
            return JsonResponse({"dummy":"User Name not found"})
    return JsonResponse({"dummy":"dummy"})
            

    