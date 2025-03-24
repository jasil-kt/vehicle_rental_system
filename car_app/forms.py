from django import forms
from django.contrib.auth.forms import UserCreationForm


from car_app.models import Login, owner, customer, vehicle, pay


class login_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = "username","password1","password2"


class owner_form(forms.ModelForm):

    class Meta:

        model = owner
        fields =  "__all__"
        exclude = ('owner_data',)



class customer_form(forms.ModelForm):

    class Meta:

        model = customer
        fields = "__all__"
        exclude = ('customer_data',)


class vehicle_form(forms.ModelForm):
     class Meta:
         model = vehicle
         fields = "__all__"
         exclude = ('owner','available')

class payment_form(forms.ModelForm):
    class Meta:
        model = pay
        fields =  "__all__"
        exclude = ('book',)