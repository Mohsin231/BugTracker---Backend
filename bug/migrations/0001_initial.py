# Generated by Django 3.1.7 on 2021-02-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('steps', models.TextField()),
                ('Priority', models.TextField()),
                ('Time', models.TextField()),
            ],
        ),
    ]
