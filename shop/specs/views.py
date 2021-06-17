from collections import defaultdict

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse

from .models import CategoryFeature, FeatureValidator, ProductFeatures
from .forms import NewCategoryFeatureKeyForm, NewCategoryForm
from mainapp.models import Category, Product



class BaseSpecView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'product_features.html', {})


class CreateNewFeatures(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        context = {'form': form}
        return render(request, 'new_feature.html', context)

    def post(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        if form.is_valid():
            new_category_feature_key = form.save(commit=False)
            new_category_feature_key.category = form.cleaned_data['category']
            new_category_feature_key.feature_name = form.cleaned_data['feature_name']
            new_category_feature_key.save()
        return HttpResponseRedirect('/product_specs/')


class CreateNewCategory(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        context = {'form': form}
        return render(request, 'new_category.html', context)

    def post(self,request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.name = form.cleaned_data['name']
            new_category.save()
        return HttpResponseRedirect('/product_specs/')


class CreateNewFeatureValidator(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'new_validator.html', context)


class FeatureChoiceView(View):

    def get(self, request, *args, **kwargs):
        option = '<option value="{value}">{option_name}</option>'
        html_select = """
        <select class="form-select"
        name="features-validators"
        id="feature-validators-id"
        aria-label="Default select example">
        <option selected>---</option>
        {result}
        </select>
        """
        feature_key_qs = CategoryFeature.objects.filter(category_id=int(request.GET.get('category_id')))
        res_string = ""
        for item in feature_key_qs:
            res_string += option.format(value=item.feature_name, option_name=item.feature_name)
        html_select = html_select.format(result=res_string)
        return JsonResponse({"result": html_select, "value": int(request.GET.get('category_id'))})
