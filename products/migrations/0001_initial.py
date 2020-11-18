# Generated by Django 3.1.3 on 2020-11-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Manufactorer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(
                    default='media/mobile-2468068_1920.png', upload_to='media/')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('latest', models.BooleanField(default=False)),
                ('best', models.BooleanField(default=False)),
                ('category', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('manufactorer', models.ForeignKey(help_text='if missing, you can add the manufactorer on the dedicated form on this page',
                                                   null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.manufactorer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CaroPics',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Caro Pics',
            },
        ),
    ]
