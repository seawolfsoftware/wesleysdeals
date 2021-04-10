# Generated by Django 3.1.7 on 2021-04-10 02:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiUseDeal',
            fields=[
                ('deal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='deals.deal')),
                ('access_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('duration', models.PositiveIntegerField()),
                ('expiry_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 10, 3, 3, 21, 784735))),
            ],
            bases=('deals.deal',),
        ),
    ]
