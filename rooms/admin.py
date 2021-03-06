from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.

@admin.register(models.RoomType,models.Facility,models.Amenity,models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self,obj):
        return obj.rooms.count()

class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):


    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name","description","country","city","address","price")},
        ),
        (
            "Times",
            {"fields":("check_in","check_out","instant_book")},
        ),
          (
            "Spaces",
            {"fields" : ("guests","beds","bedrooms","baths")}
        ),
        (
            "More About The space",
            {
                "classes" : ('collapse',),
                "fields" : ("amenities","facilities","house_rules")}
        ),
        (
            "Last Details",
            {"fields" : ("host",)}
        ),
 
    )

    list_display = (
            "name",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
            "host",
            "count_amenities",
            "count_photos",
            "total_rating",
            
        
    )
    inlines = (
        PhotoInline,
    )

    list_filter = ("amenities","host__superhost","house_rules","city",)

    search_fields = ("^city","host__username")

    ordering = ("name","price","bedrooms")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    raw_id_fields = ("host",)

    def count_amenities(self,obj):
        return obj.amenities.count()

    def count_photos(self,obj):
        return obj.photos.count()
       




@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """Photo admin """

    list_display = ('__str__','get_thumbnail',)

    def get_thumbnail(self,obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

