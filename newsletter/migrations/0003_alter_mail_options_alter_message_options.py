# Generated by Django 5.0.4 on 2024-04-19 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_mail_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение для рассылки', 'verbose_name_plural': 'Сообщения для рассылки'},
        ),
    ]
