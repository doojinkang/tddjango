from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Item

def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text = request.POST.get('item_text', ''))
        return redirect('/')

    return render(request, 'home.html')

