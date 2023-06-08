from django.shortcuts import render,redirect
from .models import product
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class Insert(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        e_name=request.GET["t2"]
        e_salary=float(request.GET["t3"])
        e_eadress=request.GET["t4"]
        p=product(eid=e_id,ename=e_name,esalary=e_salary,eadress=e_eadress,)
        e.save()
        return HttpResponse("employee inserted successfully")
class Display(View):
    def get(self,request):
        qs = product.objects.all()
        condic={"records":qs}
        return render(request,'display.html', context=condic)
class DeleteInput(View):
     def get(self,request):
        qs=product.objects.all()
        condic={"records":qs}
        return render(request, 'deleteinput.html', context=condic)
class Delete(View):
    def get(self,request):
        p_name=request.GET["t2"]
        p=product.objects.get(pname=p_name)
        p.delete()
        return redirect('/productapp/display')

class UpdateInput(View):
    def get(self,request):
        qs=product.objects.all()
        condic={"records": qs}
        return render(request,'updateinput.html',context=condic)

class UpdateDetails(View):
    def get(self,request):
        p_id=request.GET["t1"]
        prod=product.objects.get(pip=p_id)
        condic={'rec':prod}
        return render(request,'update.html',context=condic)

class Update(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.get(pip=p_id)
        prod.pname=request.GET["t2"]
        prod.pcost=float(request.GET["t3"])
        prod.pmfdt=request.GET["t4"]
        prod.expdt=request.GET["t5"]
        prod.save()
        return redirect('/productapp/display')





