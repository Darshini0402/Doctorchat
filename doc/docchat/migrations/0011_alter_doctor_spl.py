# Generated by Django 3.2.3 on 2021-11-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docchat', '0010_doctor_spl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='spl',
            field=models.CharField(max_length=4),
        ),
    ]
