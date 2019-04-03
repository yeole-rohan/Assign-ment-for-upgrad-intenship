from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


# Create your views here.
def home(request):
	todos = Todo.objects.all()
	if request.method == 'POST':
		form = TodoForm(request.POST or None)
		if form.is_valid():
			u = form.save()
			return redirect('home')
		else:
			messages.error(request,'Below field is required')
	else:
		form = TodoForm()
	return render(request, 'home.html', {'todo': todos,'form':form})


def edit(request, id):
	if request.method == 'POST':
		todo = Todo.objects.get(pk = id)
		todo.title = request.POST.get('todo')
		todo.save()
		messages.error(request,'Updated')
		return redirect('home')
	else:
		todo = Todo.objects.get(pk=id)
		return render(request, 'edit.html', {'todo': todo})


def delete(request, id):
	todo = Todo.objects.get(pk=id)
	todo.delete()
	messages.error(request,'Deleted')
	return redirect('home')