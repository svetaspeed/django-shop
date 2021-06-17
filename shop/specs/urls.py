from django.urls import path
from .views import (
    BaseSpecView,
    CreateNewCategory
)


urlpatterns = [
    path('', BaseSpecView.as_view(), name='base-spec'),
    path('new_category', CreateNewCategory.as_view(), name='new_category')
]
