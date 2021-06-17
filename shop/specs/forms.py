from django import forms

from .models import FeatureValidator, CategoryFeatures
from mainapp.models import Category


class NewCategoryFeatureKeyForm(forms.ModelForm):

    class Meta:
        model = CategoryFeatures
        fields = '__all__'


class NewCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class FeatureValidatorForm(forms.ModelForm):

    class Meta:
        model = FeatureValidator
        fields = ['category']
