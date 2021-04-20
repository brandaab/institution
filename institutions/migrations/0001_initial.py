# Generated by Django 3.2 on 2021-04-19 22:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone_no2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('fax_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('website', models.URLField()),
                ('pob', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='logos/%y')),
            ],
        ),
    ]
