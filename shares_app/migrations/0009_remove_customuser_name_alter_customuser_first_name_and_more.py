# Generated by Django 4.1 on 2023-03-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares_app', '0008_remove_customuser_bundle_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
