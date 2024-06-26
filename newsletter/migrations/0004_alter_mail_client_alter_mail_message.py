# Generated by Django 5.0.4 on 2024-04-21 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_alter_mail_options_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='message',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message', verbose_name='Сообщение'),
        ),
    ]
