from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = "This command created amenities"

    def handle(self,*args,**options):
        amenities = [
            "Air Condition",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Cable TV",
            "Chairs",
            "Sofa",
            "TV",
            "Swimming Pool",

        ]
        for a in amenities:
            Amenity.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Amenities Created!"))



    