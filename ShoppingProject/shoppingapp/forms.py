from .models import *
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model= OrderModel
        exclude=['usr','pro','order_id',
                 'payment_id','payment_status','amount','order_status']