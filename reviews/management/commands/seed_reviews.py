import random 
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from reviews.models import Review
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):
    help = "This command creates Reviews"

    def add_arguments(self,parser):
        parser.add_argument(
            "--number",default = 1, help = "How many Reviews do you want to create"
        )

    def handle(self,*args,**options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            Review,
            int(number),
            {
            "accuracy" : lambda x: random.randint(1,5),
            "communication" : lambda x: random.randint(1,5), 
            "cleanliness" : lambda x: random.randint(1,5) ,
            "location" : lambda x: random.randint(1,5),
            "check_in" : lambda x: random.randint(1,5),
            "value" : lambda x: random.randint(1,5), 
            "room" : lambda x: random.choice(rooms),
            "user" : lambda x: random.choice(users),
     
        })

        seeder.execute()
      

        self.stdout.write(self.style.SUCCESS(f"{number} Reviews Created!"))



    