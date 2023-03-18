from django.http import HttpResponse
from django.shortcuts import redirect, render


from SecondModule.models import UserData
from SecondModule.forms import UserForm
from django.contrib import messages

# Create your views here.


def SecondModule(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("DONE")
            print("DONE2")
            messages.success(request, ("ADD SUCCESSFULLY"))
        return redirect("SecondModule")

    else:
        allUserdata = UserData.objects.all
        return render(request, 'SecondHome.html', {"allUser": allUserdata})
       #   allUserdata = Userdata.objects.all
       

def deleteuser(request, user_id):
    Userdetail = UserData.objects.get(pk=user_id)
    Userdetail.delete()
    

def isadmin(request, user_id):
    Userdetail = UserData.objects.get(pk=user_id)
    Userdetail.isadmin=True
    Userdetail.save()

    return redirect('SecondModule')


def edituser(request, user_id):
    if request.method=="POST":
        Userdetail = UserData.objects.get(pk=user_id)
        form=UserForm(request.POST or None,instance=Userdetail)
        if form.is_valid():
            form.save();
        
def addEvents(request):
    context = {'texthome': "WELCOME HOME PAGE"}
    return render(request, 'addEvents.html', context)


def index(request):
    context = {'textindex': "WELCOME HOME PAGE"}
    return render(request, 'index.html', context)


def Aboutus(request):
    context = {'text': "About us page"}
    return render(request, 'SecondAboutus.html', context)
  #  return HttpResponse("This is my Second Page About us")
