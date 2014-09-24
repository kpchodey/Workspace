from django.contrib import admin

# Register your models here.

from app.models import Event, Venue, Price, Ticket, UserProfile

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Price)
admin.site.register(Ticket)
admin.site.register(UserProfile)