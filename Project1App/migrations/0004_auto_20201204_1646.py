# Generated by Django 3.0.8 on 2020-12-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project1App', '0003_auto_20201202_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='web_category',
            field=models.CharField(choices=[('WebSite type', 'Website type'), ('Static WebSite', 'Static Website'), ('Dynamic Website', 'Dynamic Website')], max_length=100, null=True),
        ),
    ]
