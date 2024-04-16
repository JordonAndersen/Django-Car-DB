# Generated by Django 5.0.4 on 2024-04-16 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_user_app', '0001_initial'),
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement_date', models.DateTimeField(auto_now_add=True)),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='car_app.car')),
                ('seller_account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app_user_app.appuser')),
            ],
        ),
    ]
