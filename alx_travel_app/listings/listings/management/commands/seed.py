import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write("Seeding database with sample listings...")

        for _ in range(10):  # Create 10 sample listings
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                price=round(random.uniform(50, 500), 2),
                location=fake.city()
            )

        self.stdout.write(self.style.SUCCESS("Database seeding complete!"))
