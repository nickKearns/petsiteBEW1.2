# Generated by Django 3.0 on 2020-05-14 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('weight_in_pounds', models.PositiveSmallIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateField(auto_now=True)),
                ('duration_minutes', models.PositiveSmallIntegerField()),
                ('special_instructions', models.CharField(max_length=256)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets.Pet')),
            ],
        ),
    ]
