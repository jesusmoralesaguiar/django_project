# Generated by Django 4.2.2 on 2023-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Overlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.SlugField(max_length=150, unique=True)),
                ('disable', models.BooleanField(default=False, help_text='Disable it, if you want hide action', verbose_name='enabled')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('file', models.CharField(max_length=150)),
                ('repository', models.CharField(max_length=150)),
                ('commit', models.CharField(max_length=150, null=True)),
                ('description', models.CharField(max_length=150)),
                ('upstream', models.BooleanField(default=False, help_text='Check this to allow other disciplines to execute this overlay through the projectfile.')),
            ],
            options={
                'verbose_name_plural': 'Overlay',
                'ordering': ['action'],
            },
        ),
    ]