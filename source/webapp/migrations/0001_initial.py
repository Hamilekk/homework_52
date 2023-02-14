# Generated by Django 4.1.6 on 2023-02-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('status', models.CharField(default= 'new', choices = [('new', 'Новая'), ('In process','В процессе'),
                                                                       ('Complete', 'Сделано')], max_length=200,
                                            verbose_name='Статус')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]
