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
                "placeholder": "Enter your Age",
                'min':1,
                'max':100,

            }),
            "course": forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Enter your Course name"
            }
            ),
        }
    def clean_age(self):
        age = self.cleaned_data['age']
        if age<1 or age>100:
            raise forms.ValidationError("Age must be between 1 and 100")
        return age