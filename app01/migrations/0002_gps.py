# Generated by Django 4.1.7 on 2023-05-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_j', models.CharField(default=116.811379, max_length=20)),
                ('gps_w', models.CharField(default=36.556447, max_length=20)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
