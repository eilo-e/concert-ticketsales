from django.shortcuts import render
from ticketsale.models import Concert,Location,TimeConcert

#from django.http import HttpResponse
# Create your views here.
def concertListView(request):
    concerts=Concert.objects.all()
    context={
        "ConcertList":concerts
    } 
    return render(request,"ticketsale/ConcertList.html",context)


def locationListView(request):
    locations=Location.objects.all()
    context={
        "locationList":locations
    } 
    return render(request,"ticketsale/Locationlist.html",context)

def ConcertDetailsView(request,concert_id):
    concert = Concert.objects.get(pk=concert_id)
    context ={
        "concertDetailes":concert,
        "concertcount":concert.count()
    }
    return render(request,"ticketsails/concertDetail.html",context)

def TimeListView(request):
    time=TimeConcert.object.all()
    context={
        "TimeList":time
    }
    return render(request,"ticketsales/TimeList.html",context)





