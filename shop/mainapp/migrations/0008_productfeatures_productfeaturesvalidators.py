# Generated by Django 3.2.1 on 2021-06-06 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210513_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_key', models.CharField(max_length=100, verbose_name='Ключ характеристики')),
                ('feature_name', models.CharField(max_length=255, verbose_name='Наименование характеристики')),
                ('postfix_for_value', models.CharField(blank=True, help_text='Например для характеристики "Часы работы" к значению можно добавить постфикс "часов", и как результат - значение "10 часов"', max_length=20, null=True, verbose_name='Постфикс для значения')),
                ('use_in_filter', models.BooleanField(default=False, verbose_name='Использовать в фильтрации товаров в шаблоне')),
                ('filter_type', models.CharField(choices=[('radio', 'Радиокнопка'), ('checkbox', 'Чекбокс')], default='checkbox', max_length=20, verbose_name='Тип фильтра')),
                ('filter_measure', models.CharField(help_text='Единица измерения для конкретного фильтраю Например "Частота процессора (Ghz).Единица измерения будет информация в скобках.', max_length=50, verbose_name='Еденица измерения для фильтра')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeaturesValidators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_value', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Значение характеристики')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
                ('feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.productfeatures', verbose_name='Характеристика')),
            ],
        ),
    ]
