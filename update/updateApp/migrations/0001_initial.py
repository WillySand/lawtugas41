# Generated by Django 4.0.4 on 2022-06-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('npm', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
