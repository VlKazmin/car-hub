# Generated by Django 3.2.18 on 2024-01-04 20:20

import cars.utils
import cars.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinatesCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Допустимый диапазон: -90.0 до 90.0', validators=[django.core.validators.MaxValueValidator(limit_value=90.0), django.core.validators.MinValueValidator(limit_value=-90.0)], verbose_name='Широта')),
                ('longitude', models.FloatField(help_text='Допустимый диапазон: -180.0 до 180.0', validators=[django.core.validators.MaxValueValidator(limit_value=180.0), django.core.validators.MinValueValidator(limit_value=-180.0)], verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Координата',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_image/default_car.png', help_text='Изображение автомобиля', upload_to=cars.utils.image_upload_to)),
                ('is_available', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=True, verbose_name='Доступна ли машина?')),
                ('company', models.CharField(choices=[('BelkaCar', 'BelkaCar'), ('YandexDrive', 'ЯндексДрайв'), ('CityDrive', 'Ситидрайв')], max_length=30, verbose_name='Название компании каршеринга')),
                ('brand', models.CharField(max_length=30, verbose_name='Марка')),
                ('model', models.CharField(max_length=30, verbose_name='Модель')),
                ('type_car', models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('minivan', 'Минивен')], max_length=30, verbose_name='Тип')),
                ('state_number', models.CharField(max_length=10, validators=[cars.validators.validate_state_number], verbose_name='Госномер')),
                ('type_engine', models.CharField(choices=[('electro', 'Электрический'), ('benzine', 'Бензин')], max_length=30, verbose_name='Тип двигателя')),
                ('child_seat', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False, verbose_name='Присутствие детского кресла')),
                ('power_reserve', models.IntegerField(verbose_name='Запас хода')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Рейтинг автомобиля')),
                ('kind_car', models.CharField(choices=[('Passenger', 'Легковой'), ('Cargo', 'Грузовой')], max_length=9, verbose_name='Вид')),
                ('coordinates', models.OneToOneField(help_text='Укажите координаты автомобиля', on_delete=django.db.models.deletion.CASCADE, related_name='car_coordinates', to='cars.coordinatescar', verbose_name='Координаты автомобиля')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
