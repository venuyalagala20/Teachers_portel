# Generated by Django 4.1.7 on 2023-03-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryapp', '0004_alter_teacher_roomnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='PhoneNumber',
            field=models.CharField(max_length=100),
        ),
    ]