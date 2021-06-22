from django.urls import path
from .views import (
    BaseSpecView,
    CreateNewCategory,
    CreateNewFeatures
)


urlpatterns = [
    path('', BaseSpecView.as_view(), name='base-spec'),
    path('new-category', CreateNewCategory.as_view(), name='new-category'),
    path('new-feature/', CreateNewFeatures.as_view(), name='new-feature')
]
