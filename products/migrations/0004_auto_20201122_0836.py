# Generated by Django 3.1.3 on 2020-11-22 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201113_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='mobile-2468068_1920.jpg', help_text='minimum 235x460 px please.', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufactorer',
            field=models.ForeignKey(help_text='if missing, you can add the manufactorer on the dedicated link under "Product Management".', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.manufactorer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='price in euro', max_digits=10),
        ),
    ]
