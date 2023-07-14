from django.shortcuts import render,redirect
import pyrebase
from .import pushdata as ps
# Create your views here.


def index(request):
    if request.method == "POST":
        time1 = request.POST['status']
        data = {
            "time1":time1,
        }
        ps.database.child("Data").child("reminder").set(data)

    return render(request,'index.html')

def status(request):
    # box1=ps.database.child("Data").child("reminder").child('box1').get().val()
    # box2=ps.database.child("Data").child("reminder").child('box2').get().val()
    time1=ps.database.child("Data").child("reminder").child('time1').get().val()
    # time2=ps.database.child("Data").child("reminder").child('time2').get().val()
    context={
        'time1':time1,
    }
    return render(request,"status.html",context)