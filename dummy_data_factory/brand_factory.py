from django.db import transaction
from garage.models import CarBrand


@transaction.atomic
def create_brands():
    brand_names = ["Toyota", "Honda", "Ford", "Tesla", "BMW"]
    # Delete existing CarBrand objects to ensure fresh start for dummy data
    CarBrand.objects.all().delete()
    brands_to_create = []
    # Creates a list of CarBrand objects
    for current_brand_name in brand_names:
        current_brand_object = CarBrand(
            name=current_brand_name,
            num_seats=4,
            num_wheel=4,
            very_very_large_data_field={}
        )
        brands_to_create.append(current_brand_object)
    CarBrand.objects.bulk_create(brands_to_create)
    return list(CarBrand.objects.all())
