# Generated by Django 3.0.8 on 2020-12-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project1App', '0010_auto_20201205_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
