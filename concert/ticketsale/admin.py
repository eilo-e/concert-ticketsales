from django.contrib import admin

# Register your models here.
from.models import Concert
admin.site.register(Concert)

from.models import Location
admin.site.register(Location)

from.models import TimeConcert
admin.site.register(TimeConcert)

from.models import Profile
admin.site.register(Profile)

from.models import TicketModel
admin.site.register(TicketModel)

