# Generated by Django 5.1.3 on 2024-12-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraisers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_fundraiser_personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('year_of_birth', models.DateField()),
            ],
        ),
    ]
