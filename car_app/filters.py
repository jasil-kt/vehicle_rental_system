import django_filters
from django import forms
from django_filters import CharFilter

from car_app.models import vehicle


class BrandFilter(django_filters.FilterSet):
    name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search name','class':'form-control'}))

    class Meta:
        model = vehicle
        fields = ('name',)

# class ownerFilter(django_filters.FilterSet):
#     product_user__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search seller','class':'form-control'}))
#     class Meta:
#         model = vehicle
#         fields = ('product_user__name',)