from django.db import models
from accounts.models import Profile

#from jalali_date import datetime2jalali,date2jalalli

# Create your models here.
class Concert(models.Model):
    title = models.CharField(max_length=50)
    timeConcert = models.TimeField()
    location = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    image = models.ImageField(max_length=2 ,upload_to= "concert/media/")


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)


class TimeConcert(models.Model):
    concert = models.ForeignKey(Concert,on_delete=models.PROTECT)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    startTime = models.TimeField()
    numberOfSeats = models.IntegerField(null=True)
#  def __str__(self):
#     return "time: {} title: {} location: {}".format(self.startTime,Concert.title,Location.address)
    start = 1
    end = 2
    cancel = 3
    sales = 4
    status_choices = (
    (start, "فروش بلیط"),
    (end, "پایان"),
    (cancel, "کنسل"),
    (sales, "کامل فروخته شده")
)
    status = models.IntegerField(choices=status_choices)
   
    def __str__(self):
        return "time: {} concert name:{} location:{}".format(self.start_time, self.concert.name, self.location.name) 

  #  def get_jalali_date(self):
   #     return datetime2jalali(self.startTime)



class TicketModel(models.Model):
    profileModel = models.ForeignKey(Profile,on_delete=models.PROTECT,max_length=20)
    timeModel = models.ForeignKey(TimeConcert,on_delete=models.PROTECT,max_length=20)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    def __str__(self):
        return "profile: {} concert time: {}".format(Profile.name,TimeConcert.startTime)