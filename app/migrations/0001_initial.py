# Generated by Django 4.1.7 on 2023-03-31 11:49

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69, validators=[app.validators.validate_string])),
                ('image', models.ImageField(upload_to='dogs/')),
            ],
        ),
    ]
