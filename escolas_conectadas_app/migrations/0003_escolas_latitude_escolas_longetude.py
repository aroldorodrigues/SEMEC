# Generated by Django 5.0.1 on 2024-04-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas_conectadas_app', '0002_escolas_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='escolas',
            name='latitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='escolas',
            name='longetude',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]