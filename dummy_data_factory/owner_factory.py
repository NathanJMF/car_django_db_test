from django.db import transaction
from garage.models import Owner
from faker import Faker


@transaction.atomic()
def create_owners(num_owners=50000, batch_size=5000):
    # Delete existing Owner objects to ensure fresh start for dummy data
    Owner.objects.all().delete()
    fake = Faker()
    owners_to_create = []
    current_count = 0
    for _ in range(num_owners):
        first_name = fake.first_name()
        last_name = fake.last_name()
        current_owner_object = Owner(first_name=first_name, last_name=last_name)
        owners_to_create.append(current_owner_object)
        current_count += 1

        # Bulk insert every batch of generated entries
        if current_count % batch_size == 0:
            Owner.objects.bulk_create(owners_to_create)
            owners_to_create = []

    # Insert any leftovers
    if owners_to_create:
        Owner.objects.bulk_create(owners_to_create)

    return list(Owner.objects.all())
