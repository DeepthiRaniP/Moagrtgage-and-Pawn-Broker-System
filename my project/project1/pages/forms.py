from django import forms

from .models import Admin, Employee, Department, Product, pawnbroker, item


class DateInput(forms.DateInput):
    input_type = "date"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {"category": "Select Category"}


class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = "__all__"
        labels = {"category": "Select Category"}


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password": forms.PasswordInput()}


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"dateofbirth": DateInput(), "password": forms.PasswordInput(),
                   'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}


class PawnbrokerRegistrationForm(forms.ModelForm):
    class Meta:
        model = pawnbroker
        fields = "__all__"
        widgets = {"dateofbirth": DateInput(), "password": forms.PasswordInput(),
                   'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Enter location of your shop'})}
