# Generated by Django 3.0.8 on 2020-12-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project1App', '0008_auto_20201204_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]