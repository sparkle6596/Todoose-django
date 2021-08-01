from django.shortcuts import render

# Create your views here.

from .forms import AddTodooForm
from todoo.models import todooses
def todo_add(request):
    context = {}
    if request.method == "GET":
        form = AddTodooForm()
        context["form"] = form
        return render(request, "todocreate.html", context)
    elif request.method == "POST":
        context = {}
        form = AddTodooForm(request.POST)

        if form.is_valid():
            context["form"] = form
            tsk_name = form.cleaned_data["task_name"]
            usr= form.cleaned_data["user"]
            status=form.cleaned_data["status"]
            print(tsk_name,status,usr)
            todoose=todooses()


        else:
            return render(request, "todocreate.html",context)


