# Generated by Django 5.0.4 on 2024-04-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='title',
            field=models.CharField(default='-', max_length=100, verbose_name='Тема рассылки'),
            preserve_default=False,
        ),
    ]