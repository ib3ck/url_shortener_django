# Generated by Django 3.1.7 on 2021-12-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]
