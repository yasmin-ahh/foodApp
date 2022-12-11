from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'
# Create your views here.
def index(request):
    item_lst = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_lst' : item_lst
    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('This is a food app')

def detail(request, id):
    item_gg = Item.objects.get(pk=id)
    #template = loader.get_template('food/details.html')
    context = {
        'item_gg' : item_gg
    }
    return render(request,'food/details.html', context)
    #return HttpResponse(template.render(context, request))
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})

#This is a class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})