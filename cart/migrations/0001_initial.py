# Generated by Django 2.2 on 2020-12-21 14:48

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(editable=False, max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=32)),
                ('street_address_1', models.CharField(max_length=50)),
                ('street_address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=32)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date', models.DateField(auto_now_add=True)),
                ('email_print', models.CharField(choices=[('Email Print', 'Email Print'), ("Please don't email Print", "Please don't email Print")], default='Email Print', max_length=30)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.Order')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo')),
            ],
        ),
    ]
