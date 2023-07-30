from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def index(request):


    items = Todo.objects.all()
    context = {
        "names": items
    }
    return render(request, "index.html", context)

def add_item(request):

    if request.method == "POST":
        
        name = request.POST.get("name")

        print(name)
        name = Todo(name = name)
        name.save()

        return redirect("/")
    
    return render(request, "index.html")

def deleteData(request,id):

    d = Todo.objects.get(id=id) 
    d.delete()
    return redirect("/") 

def updateData(request, id):

    if request.method == "POST":
        
        name = request.POST["name"]
        edit = Todo.objects.get(id=id)
        edit.name=name
        edit.save()

        return redirect("/")

    d = Todo.objects.get(id=id) 
    context = {"name":d}
    return render(request,"edit.html",context)