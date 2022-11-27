# Generated by Django 4.1.3 on 2022-11-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='projectphoto/')),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
