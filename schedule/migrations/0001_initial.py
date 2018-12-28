# Generated by Django 2.1.2 on 2018-10-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('not_available', models.BooleanField(default=False)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klass.Klass')),
            ],
        ),
    ]
