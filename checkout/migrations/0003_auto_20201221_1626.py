# Generated by Django 2.2 on 2020-12-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201221_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email_print',
            field=models.CharField(choices=[('Email Print', 'Email Print'), ("Please don't email Print", "Please Don't Email Print")], default='Email Print', max_length=30),
        ),
    ]
