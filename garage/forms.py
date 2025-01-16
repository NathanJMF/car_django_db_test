from django import forms

class CarForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    name = forms.CharField(label="Car Name", max_length=255)
    num_seats = forms.IntegerField(label="Number of Seats", min_value=1)
    num_wheel = forms.IntegerField(label="Number of Wheels", min_value=1)
