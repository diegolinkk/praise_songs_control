# Generated by Django 3.0.2 on 2020-01-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='louvor',
        ),
        migrations.AddField(
            model_name='louvor',
            name='banda',
            field=models.ManyToManyField(blank=True, to='songs.Banda'),
        ),
    ]
