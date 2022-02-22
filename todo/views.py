from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from todo.models import List
# Create your views here.
def todo(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Submit':
            task = request.POST.get('task')
            list = List(task=task)
            list.save()
            return redirect('/todolist')
        elif request.POST.get('submit') == 'Search':
            search = request.POST.get('task')
            tasks = List.objects.filter(task__contains=search)
            return render(request, 'index.html', {'tasks': tasks})
    else:
        tasks = List.objects.all()
        return render(request, 'index.html',{'tasks':tasks})

def edit(request, id):
    tasks = List.objects.all()
    if request.method =="POST":
        task = request.POST.get('task')
        list = List.objects.get(id=id)
        list.task = task
        list.save()
        return render(request, 'index.html', {'tasks': tasks})
    else:  
        etask = List.objects.get(id=id)
        return render(request, 'index.html', {'tasks': tasks, 'etask': etask})


def delete(request,id):
    task = List.objects.get(id=id)
    task.delete()
    return redirect('/todolist')