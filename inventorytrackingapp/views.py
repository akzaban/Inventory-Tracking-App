from django.shortcuts import render,redirect
from .models import Details
from .forms import detailsform

# Create your views here.
def index(request):
    return render(request,'index.html')
 
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        obj=Details.objects.create(name=name,price=price,quantity=quantity)
        obj.save()
        return redirect('/')
 
def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})

def edit(request,id): 
    object=Details.objects.get(id=id)
    return render(request,'edit.html',{'object':object})
    
def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        return redirect('retrieve')
    
def delete(request,pk):   
        query= Details.objects.filter(id=pk)
        if request.method =='POST':
            query.delete()
            return redirect('retrieve')
        return render(request,'delete_items.html')
