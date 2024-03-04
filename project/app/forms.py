from django import forms
from .models import *


class CoursesForm(forms.ModelForm):
    class Meta :
        model = Course
        fields = "__all__"