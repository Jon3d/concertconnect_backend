from django.contrib import admin
from artist.models import Artist
from ccuser.models import CCUser
from event.models import Event

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(CCUser)
class CCUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass