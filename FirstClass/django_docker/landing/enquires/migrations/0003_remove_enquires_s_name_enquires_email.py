# Generated by Django 5.0.3 on 2024-04-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquires', '0002_remove_enquires_budge_remove_enquires_confirm_budge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquires',
            name='s_name',
        ),
        migrations.AddField(
            model_name='enquires',
            name='email',
            field=models.EmailField(default='xxxxx@mail.ru', max_length=254),
        ),
    ]
