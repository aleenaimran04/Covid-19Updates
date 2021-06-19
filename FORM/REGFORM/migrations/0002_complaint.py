# Generated by Django 3.2 on 2021-06-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REGFORM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
    ]