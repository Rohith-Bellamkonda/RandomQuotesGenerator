from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import random

# Create your views here.
def index(request):
    red= ModelQuote.objects.all().count()
    r_num=random.randint(1,red)
    qt = ModelQuote.objects.filter(id=r_num)


    



    context = {"qt":qt}
    return render(request,'index.html',context)




    return render(request,'index.html')
@api_view(['GET'])
def api_show(request):
    qt= ModelQuote.objects.all()
    serializer = SerializerModelQuote(qt,many=True)
    return Response(serializer.data)
@api_view(['POST'])    
def api_add(request):
    qt= ModelQuote.objects.all()
    serializer = SerializerModelQuote(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)

@api_view(['POSt'])    
def api_update(request,id):
    qt= ModelQuote.objects.get(id=id)
    serializer = SerializerModelQuote(instance=qt,data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)
@api_view(['DELETE'])
def api_delete(request,id):
    qt= ModelQuote.objects.get(id=id)
    qt.delete()
    return Response("DELETION SUCCESS")