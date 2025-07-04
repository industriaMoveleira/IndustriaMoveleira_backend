# Generated by Django 5.2.3 on 2025-06-23 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_productionorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='core.product')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='core.materiaprima')),
            ],
        ),
    ]
