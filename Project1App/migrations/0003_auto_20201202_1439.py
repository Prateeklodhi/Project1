# Generated by Django 3.0.8 on 2020-12-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project1App', '0002_auto_20201201_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='web_category',
            field=models.CharField(choices=[('Static WebSite', 'Static Website'), ('Dynamic Website', 'Dynamic Website')], max_length=100, null=True),
        ),
    ]
