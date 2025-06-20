# Generated by Django 5.2.3 on 2025-06-15 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndustryApp', '0002_machine_man'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('metal', 'Metal'), ('plastic', 'Plastic'), ('wood', 'Wood'), ('glass', 'Glass')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('machines', models.ManyToManyField(to='IndustryApp.machine')),
                ('responsible_man', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='methods', to='IndustryApp.man')),
            ],
        ),
        migrations.CreateModel(
            name='MachineUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IndustryApp.machine')),
                ('man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IndustryApp.man')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IndustryApp.method')),
            ],
        ),
    ]
