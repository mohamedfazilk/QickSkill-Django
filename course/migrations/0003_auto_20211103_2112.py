# Generated by Django 3.2.6 on 2021-11-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20211103_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
