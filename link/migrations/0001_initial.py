# Generated by Django 3.2.8 on 2021-10-20 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreUrlDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('uuid', models.CharField(max_length=10)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]