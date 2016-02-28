from django import forms

from WebApp.models import *

class CarModelForm(forms.ModelForm):

    class Meta:

        model = Car

        fields = ['car_owner', 'car_name', 'car_color', 'car_size', ]

        widgets = {'car_name': forms.TextInput}

    def clean(self):
        cleaned_data = super(CarModelForm, self).clean()

        print(cleaned_data.get('car_owner'))
        print(cleaned_data.get('car_name'))
        print(cleaned_data.get('car_color'))
        print(cleaned_data.get('car_size'))

        return cleaned_data

    def clean_car_owner(self):
        car_owner = self.cleaned_data.get('car_owner')

        if not car_owner:
            print("Please type in car_owner.")
            raise forms.ValidationError("Please type in car_owner.")

        return car_owner

    def clean_car_name(self):
        car_name = self.cleaned_data.get('car_name')

        if not car_name:
            print("Please type in car_name.")
            raise forms.ValidationError("Please type in car_name.")

        return car_name

    def clean_car_color(self):
        car_color = self.cleaned_data.get('car_color')

        if not car_color:
            print("Please type in car_color.")
            raise forms.ValidationError("Please type in car_color.")

        return car_color

    def clean_car_size(self):
        car_size = self.cleaned_data.get('car_size')

        if not car_size:
            print("Please type in car_size.")
            raise forms.ValidationError("Please type in car_size.")

        return car_size