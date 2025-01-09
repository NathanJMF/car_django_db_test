import random
from django.db import transaction
from garage.models import Car


@transaction.atomic()
def create_cars(num_cars=1000000, owners=None, brands=None, batch_size=10000):
    if owners is None or not owners:
        raise ValueError("Please provide a non-empty list of owners.")
    if brands is None or not brands:
        raise ValueError("Please provide a non-empty list of brands.")

    Car.objects.all().delete()

    cars_to_create = []
    current_count = 0

    for _ in range(num_cars):
        owner = random.choice(owners)
        brand = random.choice(brands)
        current_car_object = Car(owner=owner, brand=brand)
        cars_to_create.append(current_car_object)
        current_count += 1

        # Bulk insert every batch of generated entries
        if current_count % batch_size == 0:
            Car.objects.bulk_create(cars_to_create)
            cars_to_create.clear()

    # Insert any leftovers
    if cars_to_create:
        Car.objects.bulk_create(cars_to_create)

    return list(Car.objects.all())
