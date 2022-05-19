# Generated by Django 4.0.4 on 2022-05-18 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_alter_race_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='title',
        ),
        migrations.AddField(
            model_name='race',
            name='action',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='race_actions', to='wiki.field'),
        ),
        migrations.AddField(
            model_name='race',
            name='armor_class',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='charisma',
            field=models.IntegerField(default=0, verbose_name='charisma bonus'),
        ),
        migrations.AddField(
            model_name='race',
            name='constitution',
            field=models.IntegerField(default=0, verbose_name='constitution bonus'),
        ),
        migrations.AddField(
            model_name='race',
            name='danger',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='dexterity',
            field=models.IntegerField(default=0, verbose_name='dexterity bonus'),
        ),
        migrations.AddField(
            model_name='race',
            name='feature',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='race_features', to='wiki.field'),
        ),
        migrations.AddField(
            model_name='race',
            name='health_points',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='ideology',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='intelligence',
            field=models.IntegerField(default=0, verbose_name='intelligence bonus'),
        ),
        migrations.AddField(
            model_name='race',
            name='languages',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='race',
            name='move_speed',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='size',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='race',
            name='strength',
            field=models.IntegerField(default=0, verbose_name='strength bonus'),
        ),
        migrations.AddField(
            model_name='race',
            name='susceptibility',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='race',
            name='wisdom',
            field=models.IntegerField(default=0, verbose_name='wisdom bonus'),
        ),
        migrations.AlterField(
            model_name='bestiary',
            name='action',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bestiary_actions', to='wiki.field'),
        ),
        migrations.AlterField(
            model_name='bestiary',
            name='feature',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bestiary_features', to='wiki.field'),
        ),
        migrations.AlterField(
            model_name='race',
            name='about',
            field=models.TextField(),
        ),
    ]