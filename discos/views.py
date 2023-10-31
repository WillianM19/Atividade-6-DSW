from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import disc
from .forms import CreateDisc

def index(request):
	return render(request, 'index.html', {'discs': disc.objects.all()})


def createDisc(request):
	if request.method == "POST":
		form = CreateDisc(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			return render(request, 'createDisc.html', {'form': form})
	else:
		form = CreateDisc()
   
	return render(request, 'createDisc.html', {'form': form})

def editDisc(request, id):
   discUni = disc.objects.get(id=id)
   form = CreateDisc(request.POST, instance=discUni)
   if request.method == "POST":
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
       else:
           return render(request, 'editDisc.html', {'form': form, 'disc': discUni})
   else:
       form = CreateDisc(instance=discUni)
       return render(request, 'editDisc.html', {'form': form, 'disc': discUni})
   
def deleteDisc(request, id):
	discUni = disc.objects.get(id=id)
	discUni.delete()
	return HttpResponseRedirect('/')

def showDisc(request, id):
    discUni = disc.objects.get(id=id)
    return render(request, 'showDisc.html', {'disc': discUni})