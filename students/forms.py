from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model =Student

        fields =["full_name",
                 "email",
                 "age",
                 "course",]
        widgets = {
            "full_name" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder" : "Enter your full name"
            }),
            "email": forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder" : "Enter your Email"
            }),
            "age" : forms.NumberInput(attrs={
                "class" : "form-control",
                "placeholder": "Enter your Age"
            }),
            "course": forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Enter your Course name"
            }
            ),
        }