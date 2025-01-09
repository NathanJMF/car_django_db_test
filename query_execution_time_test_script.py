import time
import os
import django


def main():
    from garage.models import (get_cars_with_brands, get_cars_with_brands_with_join,
                               get_cars_with_brands_with_join_and_reduced_key,
                               get_cars_with_brands_with_join_and_reduced_values,
                               get_cars_with_brands_with_join_reduced_key_and_reduced_values,
                               get_cars_with_brands_without_orm_objects)
    # Commented out as it is very slow

    # start_time = time.time()
    # car_brand_objects = get_cars_with_brands()
    # end_time = time.time()
    # print("\nNaive approach:")
    # print(f"Number of cars: {len(car_brand_objects)}")
    # print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    car_brand_objects = get_cars_with_brands_with_join()
    end_time = time.time()
    print("\nJoin approach:")
    print(f"Number of cars: {len(car_brand_objects)}")
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    car_brand_objects = get_cars_with_brands_with_join_and_reduced_key()
    end_time = time.time()
    print("\nJoin + Reduced Key approach:")
    print(f"Number of cars: {len(car_brand_objects)}")
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    car_brand_objects = get_cars_with_brands_with_join_and_reduced_values()
    end_time = time.time()
    print("\nJoin + Reduced Values approach:")
    print(f"Number of cars: {len(car_brand_objects)}")
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    car_brand_objects = get_cars_with_brands_with_join_reduced_key_and_reduced_values()
    end_time = time.time()
    print("\nJoin + Reduced Key + Reduced Values approach:")
    print(f"Number of cars: {len(car_brand_objects)}")
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    car_brand_objects = get_cars_with_brands_without_orm_objects()
    end_time = time.time()
    print("\nNo ORM objects approach:")
    print(f"Number of cars: {len(car_brand_objects)}")
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')
    django.setup()
    main()
