from django.shortcuts import render,redirect,get_object_or_404
from base.models import Item,Budget_title
from .forms import ItemForm,titleForm
# Create your views here.
def Home(request):
    titles = Budget_title.objects.all()
    context = {'budgets':titles}
    return render(request,'base/home.html',context)

def create_budget(request):
    form = titleForm
    if request.method == 'POST':
        form = titleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = titleForm()
    context = {'form':form}
    return render(request,'base/budget_title.html',context)
        
def Items(request, pk, name):
    budget = get_object_or_404(Budget_title, id=pk, name=name) 
    items = budget.item_set.all()
    
    amt = sum(item.total_price for item in items)
    
    if request.method == 'POST':
        item_name = request.POST['name']
        quantity = int(request.POST['quant'])
        price = int(request.POST['peritem'])
        total_price = quantity * price
        budget.item_set.create(
            item_name=item_name,
            quantity=quantity,
            price_per_item=price,
            total_price=total_price
        )
        return redirect('items', name=budget.name, pk=budget.id)
    
    context = {
        'budget': budget,
        'items': items,
        'amt': f"{amt:,}"
    }
    return render(request, 'base/items.html', context)

def add_item(request):
    form = ItemForm
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
            item = form.save()
            item.save()
            return redirect('home')
    else:
        form = ItemForm()
    context = {'form':form}
    return render(request,'base/additem.html',context)

def remove_item(request, pk):
    item = get_object_or_404(Item, id=pk)
    budget = item.title  
    item.delete()
    return redirect('items', name=budget.name, pk=budget.id)

def edit_item(request,pk):
    item = get_object_or_404(Item,id=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quant']
        price = request.POST['peritem']
        item.item_name = name
        item.quantity = quantity
        item.price_per_item = price
        item.total_price = int(quantity)*int(price)
        item.save()
        return redirect('home')
    else:
        form = ItemForm(instance=item)
    context = {'form':form,'item':item}
    return render(request,'base/edit.html',context)