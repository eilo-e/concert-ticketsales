from django.contrib import admin
from django.urls import path
from ticketsale import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('concert/list',views.concertListView),
    path('locations/list',views.locationListView),
    path('Concert/<int:concert_id>',views.ConcertDetailsView),
    path('TimeConcert/list',views.TimeListView)
]
