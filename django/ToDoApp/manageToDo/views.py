from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import ToDoList
from .forms import ToDoListForm

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ToDoListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = ToDoList.objects.all()
            messages.success(request, (' Item has been Added to To-Do List ! '))

            return render(request, 'manageToDo/index.html', {'all_items': all_items})

    else:
        all_items = ToDoList.objects.all()

        return render(request, 'manageToDo/index.html', {'all_items': all_items})


def delete(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been Deleted !'))

    # redirect( 'link' )
    return redirect( reverse('manageToDo:home') )


def cross(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = True
    item.save()

    return redirect( reverse('manageToDo:home') )

def uncross(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = False
    item.save()

    return redirect( reverse('manageToDo:home') )
