# Generated by Django 2.2.3 on 2019-10-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cultivo_main', '0014_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pred_one',
            name='Gross_Production_Value_constant_2004_2006_million_US_dollar',
        ),
        migrations.RemoveField(
            model_name='pred_one',
            name='org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar',
        ),
    ]
