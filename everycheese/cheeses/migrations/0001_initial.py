# Generated by Django 3.1.1 on 2023-11-07 02:15

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Cheese')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Cheese Address')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('firmness', models.CharField(choices=[('unspecifed', 'Unspecifed'), ('soft', 'Soft'), ('semi-soft', 'Semi-soft'), ('semi-hard', 'Semi-hard'), ('hard', 'Hard')], default='unspecifed', max_length=20, verbose_name='Frimness')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
