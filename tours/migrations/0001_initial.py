# Generated by Django 2.2 on 2020-12-28 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.CharField(choices=[('Wild Atlantic Way', 'Wild Atlantic Way'), ('French Riviera', 'French Riviera')], max_length=20)),
                ('date_preference', models.CharField(choices=[('July', 'July'), ('August', 'August')], max_length=20)),
                ('analogue_or_digital', models.CharField(choices=[('Analogue', 'Analogue'), ('Digital', 'Digital')], max_length=20)),
                ('skill_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Professional', 'Professional')], max_length=20)),
                ('dietary_requirements', models.CharField(choices=[('None', 'None'), ('Vegetarian', 'Vegetarian'), ('VEGAN', 'Vegan')], max_length=20)),
                ('any_comments', models.TextField(max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
