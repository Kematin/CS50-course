# Generated by Django 4.1.4 on 2023-01-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
    ]
