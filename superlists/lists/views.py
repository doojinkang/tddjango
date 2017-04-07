from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Item

import json
from django.core import serializers

def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text = request.POST.get('item_text', ''))
        return redirect('/')

    items = {} # Item.objects.all()
    return render(request, 'home.html', { 'items': items })

def ajax_list(request):
    items = Item.objects.all()
    data = serializers.serialize('json', items)
    return HttpResponse(data)
    
#    ret =  '"[{\\"model\\": \\"lists.item\\", \\"pk\\": 1, \\"fields\\": {\\"text\\": \\"Buy peacock feathers\\"}}, {\\"model\\": \\"lists.item\\", \\"pk\\": 2, \\"fields\\": {\\"text\\": \\"Use peacock feathers to make a fly\\"}}]"'
#    return HttpResponse(ret)


