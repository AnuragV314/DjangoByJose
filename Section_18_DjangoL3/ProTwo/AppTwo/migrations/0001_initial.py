# Generated by Django 3.2.20 on 2023-09-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=245)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
