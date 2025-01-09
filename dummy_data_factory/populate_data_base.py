from dummy_data_factory.brand_factory import create_brands
from dummy_data_factory.owner_factory import create_owners
from dummy_data_factory.car_factory import create_cars


def populate_dummy_data():
    print("Creating brands...")
    brands = create_brands()

    print("Creating owners...")
    owners = create_owners(num_owners=50000, batch_size=5000)

    print("Creating cars...")
    cars = create_cars(
        num_cars=1000000,
        owners=owners,
        brands=brands,
        batch_size=10000
    )

    print("All done!")
    return {
        "brands_count": len(brands),
        "owners_count": len(owners),
        "cars_count": len(cars),
    }
