from django.db import models


class CategoryFeatures(models.Model):
    """
    Характеристика конкретной категории
    """
    category = models.ForeignKey('mainapp.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100, verbose_name='Имя характеристики')
    feature_filter_name = models.CharField(max_length=50, verbose_name='Имя для фильтра')
    unit = models.CharField(max_length=50, verbose_name='Еденица измерения', null=True, blank=True)

    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')

    def __str__(self):
        return f"{self.category.name} | {self.feature_name}"


class FeatureValidator(models.Model):
    """
    Валидатор значений для конкрейтной характеристики принадлежащей к конкретной категории
    """
    category = models.ForeignKey('mainapp.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_key = models.ForeignKey(CategoryFeatures, verbose_name='Ключ характеристики', on_delete=models.CASCADE)
    valid_feature_value = models.CharField(max_length=100, verbose_name='Влаидное значение')

    def __str__(self):
        return f"Категория \"{self.category.name}\" | " \
               f"Характеристика \"{self.feature_key.feature_name}\" | " \
               f" Валидное значение \"{self.valid_feature_value}\""

class ProductFeatures(models.Model):
    """
    Характеристики товара
    """
    product = models.ForeignKey('mainapp.Product', verbose_name='Товар', on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeatures, verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return f"Товар - \"{self.product.title} |" \
               f"Характеристика- \"{self.feature.feature_name} |" \
               f"Значение - {self.value}"
