# Generated by Django 4.0.5 on 2022-07-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calented_api', '0005_calevent_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calevent',
            name='date_time',
            field=models.CharField(editable=False, max_length=32, null=True),
        ),
    ]