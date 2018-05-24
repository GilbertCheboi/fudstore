from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    """
    User-related CRUD form
    """
    class Meta:
        model = Address
        fields = [
            'nickname',
            'name',
            #'billing_profile',
            'address_type',
            'phone_number_1',
            'phone_number_2',
            'city',
            'country',
            'Estate',
            'postal_code'
        ]




class AddressCheckoutForm(forms.ModelForm):
    """
    User-related checkout address create form
    """
    class Meta:
        model = Address
        fields = [
            'nickname',
            'name',
            #'billing_profile',
            #'address_type',
            'phone_number_1',
            'phone_number_2',
            'city',
            'country',
            'Estate',
            'postal_code'
        ]
