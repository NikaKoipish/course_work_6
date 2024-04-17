from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(verbose_name='Электронный адрес')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.first_name}{self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    message_title = models.CharField(max_length=100, verbose_name='Тема письма')
    message_content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return f'{self.message_title}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Mail(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='Клиент')
    mail_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Первая отправка рассылки')
    mail_periodicity = models.IntegerField(verbose_name='Периодичность')
    mail_status = models.BooleanField(default=False, verbose_name='Статус отправки')
    def __str__(self):
        return f'{self.mail_status}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'