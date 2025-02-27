# Generated by Django 5.1.4 on 2025-01-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(default=None, max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.CharField(choices=[('Pizza', 'Пицца'), ('Rolls', 'Роллы'), ('Drinks', 'Напитки')], max_length=30, null=True)),
            ],
        ),
    ]
