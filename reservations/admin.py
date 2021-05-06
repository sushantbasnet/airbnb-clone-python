from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    
    list_display = (
        "room","check_in","check_out","status","guest","in_progress","is_finished"
    )

    list_filter = ( 
        "status",
    )
