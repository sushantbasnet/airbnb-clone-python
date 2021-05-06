from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):
    help = "This command created Facilites"

    def handle(self,*args,**options):
        facilites = [
           "Private Entrance",
           "Paid Parking on premises",
           "Elevator",
           "Parking",
           "Gym",

        ]
        for a in facilites:
            Facility.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Facilites Created!"))



    