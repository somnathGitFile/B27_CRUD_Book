from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def bookView(request):
    form = BookForm()
    template_name = 'app1/book.html'
    context = {'form': form}
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showbook_url')
    return render(request, template_name, context)

def showbookView(request):
    data = Book.objects.all()
    template_name = 'app1/showbook.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updatebookView(request, id):
    obj = Book.objects.get(bid=id)
    template_name = 'app1/book.html'
    form = BookForm(instance=obj)
    context = {'form': form}
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showbook_url')
    return render(request, template_name, context)


def deletebookView(request, id):
    obj = Book.objects.get(bid=id)
    template_name = 'app1/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showbook_url')
    return render(request, template_name, context)

