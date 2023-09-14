from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
def home(response,id):
    ls=ToDoList.objects.get(id=id)
    return render(response,"main/home.html",{"name":ls.name})

def v1(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("%s" % ls.item_set.get())
def v2(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("%s" % ls.name)

def viewList(response,id):
    ls=ToDoList.objects.get(id=id)
    if response.method=="POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get('c'+str(item.id))=="clicked":
                    item.complete=True
                else:
                    item.complete=False
                item.save()
        elif response.POST.get("newItem"):
            txt=response.POST.get('new')
            if len(txt)>2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("Invalid Input")
    return render(response,"main/list.html",{"ls":ls})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            try:
                t.save()
                request.user.todolist.add(t)
                return HttpResponseRedirect("/%i" % t.id)
            except Exception as e:
                # Log or print the exception to identify the specific issue
                print("Error while saving ToDoList:", e)
        else:
            # Log or print form validation errors for debugging
            print("Form validation errors:", form.errors)
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form": form})

def view(response):
    return render(response,"main/view.html",{})