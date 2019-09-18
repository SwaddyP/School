from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import stud
# Create your views here.
# These are the python functions 
def index(request):
    students = stud.objects.all().filter(roll="36754")
    context = {'students': students}
    return render(request, 'index.html',context)
def noragami(request):
    return HttpResponse("I love the noragami series!")
def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        sem = request.POST.get("sem")
        print(name, roll, sem)
        s = stud(naam = name, roll=int(roll), sem=int(sem))
        try:
            s.save()
        except:
            return HttpResponse("roll no exists")
        return HttpResponse("Your Form has been Submitted")
    else:
        return render(request, "create.html")