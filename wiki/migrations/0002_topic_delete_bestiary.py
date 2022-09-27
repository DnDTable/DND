# Generated by Django 4.1.1 on 2022-09-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('subclass', models.CharField(choices=[('race', 'Race'), ('class', 'Class'), ('items', 'Items'), ('spells', 'Spells')], max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Bestiary',
        ),
    ]
