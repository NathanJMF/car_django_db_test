from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    num_seats = models.PositiveIntegerField()
    num_wheel = models.PositiveIntegerField()
    very_very_large_data_field = models.JSONField()


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


def get_cars_with_brands() -> dict['Car', dict[str, str]]:
    cars = Car.objects.all()
    return {
        car: {
            'owner_name': car.owner.name,
            'brand': car.brand.name
        }
        for car in cars
    }
