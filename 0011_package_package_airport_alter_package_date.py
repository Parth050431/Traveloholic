# Generated by Django 4.1.7 on 2023-03-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_extras_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_airport',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='date',
            field=models.DateField(verbose_name='%d.%m.%Y'),
        ),
    ]
