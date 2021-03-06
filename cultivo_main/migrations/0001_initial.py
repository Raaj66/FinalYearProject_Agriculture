# Generated by Django 2.1.1 on 2018-11-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=15)),
                ('GPValue_thousand_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('NPValue_thousand_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue1_million_slc', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue2_million_slc', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue1_million_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue2_million_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='pred_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=15)),
                ('GPValue_thousand_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('NPValue_thousand_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue1_million_slc', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue2_million_slc', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue1_million_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
                ('GPValue2_million_dollar', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='prod_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=25)),
                ('crop', models.CharField(max_length=25)),
                ('org_val', models.DecimalField(decimal_places=4, max_digits=12)),
                ('pred_val', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=15)),
                ('production', models.IntegerField()),
                ('imports', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('export', models.IntegerField()),
                ('seed', models.IntegerField()),
                ('domestic', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=25)),
                ('area', models.IntegerField()),
                ('yieldd', models.IntegerField()),
                ('production', models.IntegerField()),
            ],
        ),
    ]
