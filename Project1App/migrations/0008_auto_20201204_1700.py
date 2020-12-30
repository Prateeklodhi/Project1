# Generated by Django 3.0.8 on 2020-12-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project1App', '0007_auto_20201204_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='web_category',
            field=models.CharField(choices=[('Website type', '--Select Website type'), ('Static WebSite', 'Static Website'), ('Dynamic Website', 'Dynamic Website')], default='Website type', max_length=100, null=True),
        ),
    ]
