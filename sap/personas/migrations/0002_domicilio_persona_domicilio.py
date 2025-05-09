# Generated by Django 5.2.1 on 2025-05-09 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('no_calle', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.domicilio'),
        ),
    ]
