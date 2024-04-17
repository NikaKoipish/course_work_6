# Generated by Django 5.0.4 on 2024-04-17 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('message_content', models.TextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Первая отправка рассылки')),
                ('mail_periodicity', models.IntegerField(verbose_name='Периодичность')),
                ('mail_status', models.BooleanField(default=False, verbose_name='Статус отправки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='newsletter.client', verbose_name='Клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
    ]
