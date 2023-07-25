# Generated by Django 4.2.2 on 2023-07-17 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('overlay', '0001_initial'),
        ('physics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='overlay',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='physics.discipline', verbose_name='Discipline'),
        ),
    ]
